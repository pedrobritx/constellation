#!/usr/bin/env python3
"""Install/verify only Constellation-owned files; never configure providers."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import tomllib
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = Path('skills/constellation-workflow')
PROFILES = ('builder', 'designer', 'security', 'reviewer')


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def files() -> dict[Path, Path]:
    for base in (ROOT / '.agents/skills/constellation-workflow', ROOT / 'toolkit/agents'):
        for parent in [base, *base.parents]:
            if parent.is_symlink():
                raise ValueError(f'Refusing symlink source directory: {parent}')
            if parent == ROOT:
                break
        if any(p.is_symlink() for p in base.rglob('*')):
            raise ValueError(f'Refusing symlink source in {base}')
    sources = {SKILL / p.relative_to(ROOT / '.agents/skills/constellation-workflow'): p
               for p in (ROOT / '.agents/skills/constellation-workflow').rglob('*') if p.is_file()}
    for role in PROFILES:
        p = ROOT / 'toolkit/agents' / f'constellation-{role}.toml'
        if not p.is_file():
            raise ValueError(f'Missing required profile: {p.name}')
        data = tomllib.loads(p.read_text())
        if set(data) != {'name', 'description', 'developer_instructions'} or any(
                not isinstance(v, str) or not v.strip() for v in data.values()):
            raise ValueError(f'Invalid or non-inheriting agent: {p.name}')
        if data['name'] != p.stem:
            raise ValueError(f'Agent name/filename mismatch: {p.name}')
        sources[Path('agents') / p.name] = p
    if not sources or not (ROOT / '.agents/skills/constellation-workflow/SKILL.md').is_file():
        raise ValueError('Missing workflow source')
    return sources


def safe_target(home: Path, relative: Path) -> Path:
    target = home / relative
    for p in [target, *target.parents]:
        if p.is_symlink():
            raise ValueError(f'Refusing symlink target: {p}')
        if p == home:
            break
    if target.exists() and not target.is_file():
        raise ValueError(f'Refusing non-file target: {target}')
    if target.exists() and target.stat().st_nlink > 1:
        raise ValueError(f'Refusing hardlinked target: {target}')
    return target


def verify(home: Path) -> bool:
    ok = True
    for rel, src in sorted(files().items()):
        target = safe_target(home, rel)
        same = target.is_file() and digest(target) == digest(src)
        print(f'{"MATCH" if same else "MISSING/DIFFERENT"} {rel}')
        ok = ok and same
    return ok


def install(home: Path, update: bool) -> None:
    source = files()
    targets = {rel: safe_target(home, rel) for rel in source}
    changed = [rel for rel, dest in targets.items() if dest.exists() and digest(dest) != digest(source[rel])]
    if changed and not update:
        raise ValueError('Existing differing files: review first, then use --update with authorization')
    stamp = str(time.time_ns())
    backup = home / 'constellation-backups' / stamp
    # Check all paths before the first write; reject redirected metadata/backup locations too.
    receipt = safe_target(home, Path('constellation-install.json'))
    for rel in changed:
        safe_target(home, Path('constellation-backups') / stamp / rel)
    for rel in changed:
        dest = backup / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(targets[rel], dest)
    for rel, src in source.items():
        dest = targets[rel]
        if dest.exists() and digest(dest) == digest(src):
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
    revision = subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], text=True).strip()
    dirty = bool(subprocess.check_output(['git', '-C', str(ROOT), 'status', '--porcelain'], text=True))
    data = {'source': str(ROOT), 'revision': revision, 'dirty': dirty,
            'files': {str(rel): digest(src) for rel, src in source.items()}}
    if changed:
        data['backup'] = str(backup)
    elif receipt.exists():
        previous = json.loads(receipt.read_text())
        if 'backup' in previous:
            data['backup'] = previous['backup']
    receipt.parent.mkdir(parents=True, exist_ok=True)
    receipt.write_text(json.dumps(data, indent=2) + '\n')
    print(f'Installed {len(source)} owned files; backed up {len(changed)} changed files.')


def connections(home: Path) -> None:
    config = home / 'config.toml'
    data = tomllib.loads(config.read_text()) if config.exists() else {}
    # Deliberately omit URLs, commands, arguments, headers and environment values.
    for name, item in data.get('mcp_servers', {}).items():
        print(json.dumps({'name': name, 'transport': 'http' if 'url' in item else 'stdio',
                          'enabled': item.get('enabled', True), 'status': 'configured, runtime unverified'}))


def package(output: Path) -> None:
    source_files = files()
    manifest = ROOT / 'toolkit/plugin.json'
    if manifest.is_symlink():
        raise ValueError('Refusing symlink plugin manifest')
    data = json.loads(manifest.read_text())
    if len(data['extensions']['com.openai']['interface']['shortDescription']) > 30:
        raise ValueError('Plugin subtitle exceeds 30 characters')
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
        archive.write(manifest, 'plugin.json')
        for rel, source in source_files.items():
            if rel.parts[0] == 'skills':
                archive.write(source, str(rel))
    with zipfile.ZipFile(output) as archive:
        if archive.testzip():
            raise ValueError('Corrupt plugin archive')
        print('Packaged:', ', '.join(archive.namelist()))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['install', 'verify', 'connections', 'package'])
    parser.add_argument('--home', type=Path, default=Path(os.environ.get('CODEX_HOME', Path.home() / '.codex')))
    parser.add_argument('--update', action='store_true', help='Back up and replace differing owned files after review')
    parser.add_argument('--output', type=Path, help='Archive path for package')
    args = parser.parse_args()
    try:
        if args.action == 'package':
            if args.output is None:
                raise ValueError('package requires --output')
            package(args.output)
        elif args.action == 'install':
            install(args.home.absolute(), args.update)
        elif args.action == 'verify':
            return 0 if verify(args.home.absolute()) else 1
        else:
            connections(args.home.absolute())
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
