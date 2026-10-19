"""Exercise installation preservation and drift reporting in disposable homes."""
import importlib.util
from pathlib import Path
import tempfile
import shutil
import os
from unittest.mock import patch
import unittest

spec = importlib.util.spec_from_file_location('toolkit', Path(__file__).parents[1] / 'automation/toolkit.py')
toolkit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(toolkit)


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name)

    def test_install_preserves_unrelated_files_and_is_repeatable(self):
        config = self.home / 'config.toml'
        config.write_text('unrelated = true\n')
        toolkit.install(self.home, False)
        toolkit.install(self.home, False)
        self.assertTrue(toolkit.verify(self.home))
        self.assertEqual(config.read_text(), 'unrelated = true\n')
        self.assertFalse((self.home / 'constellation-backups').exists())

    def test_drift_requires_update_and_retains_backup(self):
        toolkit.install(self.home, False)
        target = self.home / 'skills/constellation-workflow/SKILL.md'
        target.write_text('local work')
        self.assertFalse(toolkit.verify(self.home))
        with self.assertRaises(ValueError):
            toolkit.install(self.home, False)
        self.assertEqual(target.read_text(), 'local work')
        toolkit.install(self.home, True)
        backups = list((self.home / 'constellation-backups').rglob('SKILL.md'))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(), 'local work')
        self.assertTrue(toolkit.verify(self.home))

    def test_symlink_parent_rejected_before_any_write(self):
        outside = self.home / 'outside'
        outside.mkdir()
        (self.home / 'skills').symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ValueError):
            toolkit.install(self.home, True)
        self.assertEqual(list(outside.iterdir()), [])
        self.assertFalse((self.home / 'agents').exists())

    def test_unrelated_agent_preserved(self):
        (self.home / 'agents').mkdir()
        unrelated = self.home / 'agents/personal.toml'
        unrelated.write_text('private settings')
        toolkit.install(self.home, False)
        self.assertEqual(unrelated.read_text(), 'private settings')

    def test_nonfile_target_rejected_before_write(self):
        (self.home / 'agents/constellation-builder.toml').mkdir(parents=True)
        with self.assertRaises(ValueError):
            toolkit.install(self.home, True)
        self.assertFalse((self.home / 'skills').exists())

    def test_hardlinked_target_and_receipt_rejected(self):
        toolkit.install(self.home, False)
        for rel in ['agents/constellation-builder.toml', 'constellation-install.json']:
            target = self.home / rel
            unrelated = self.home / ('unrelated-' + target.name)
            os.link(target, unrelated)
            previous = unrelated.read_bytes()
            with self.assertRaises(ValueError):
                toolkit.install(self.home, True)
            self.assertEqual(unrelated.read_bytes(), previous)
            unrelated.unlink()

    def source_fixture(self):
        root = self.home / 'source'
        shutil.copytree(toolkit.ROOT / '.agents', root / '.agents')
        shutil.copytree(toolkit.ROOT / 'toolkit', root / 'toolkit')
        return root

    def test_symlink_source_rejected_for_install_and_package(self):
        root = self.source_fixture()
        private = self.home / 'private.txt'
        private.write_text('synthetic secret')
        (root / '.agents/skills/constellation-workflow/leak.txt').symlink_to(private)
        with patch.object(toolkit, 'ROOT', root):
            with self.assertRaises(ValueError):
                toolkit.install(self.home / 'destination', False)
            with self.assertRaises(ValueError):
                toolkit.package(self.home / 'package.zip')
        self.assertFalse((self.home / 'destination').exists())
        self.assertFalse((self.home / 'package.zip').exists())

    def test_missing_profile_fails_verification(self):
        root = self.source_fixture()
        (root / 'toolkit/agents/constellation-reviewer.toml').unlink()
        with patch.object(toolkit, 'ROOT', root):
            with self.assertRaises(ValueError):
                toolkit.verify(self.home)



if __name__ == '__main__':
    unittest.main()
