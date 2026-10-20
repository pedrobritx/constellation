# Lightweight Constellation workflow in Codex

The first usable slice is a normal skill: [constellation-workflow](../.agents/skills/constellation-workflow/SKILL.md). Invoke `$constellation-workflow` with an idea, existing project request or request to resume. Codex investigates, recommends, discusses consequential choices, builds authorized work and leaves project-owned continuity. No standalone app, paid provider, service or pilot selection is required.

## Installation and discovery

The maintained source is `.agents/skills/constellation-workflow/`. Repo-local discovery applies in a Codex session that discovers this repository's skills; this folder alone is not globally available in unrelated projects.

Use Python 3.11+ (standard library only) from the repository root:

```sh
python3 automation/toolkit.py install
python3 automation/toolkit.py verify
python3 automation/toolkit.py connections
python3 -m unittest discover -s tests -v
python3 automation/toolkit.py package --output /absolute/output/constellation-toolkit.zip
```

The installer adds the workflow to `${CODEX_HOME:-$HOME/.codex}/skills/constellation-workflow` and four standalone TOML profiles to the same home's `agents/`. Existing differing files cause a stop. Review their diffs first; an authorized `install --update` backs up changed owned files under `constellation-backups/` before replacement. Unrelated files are preserved and no files are deleted. `constellation-install.json` records source revision, dirty state, hashes and backup location; `verify` compares current source bytes rather than trusting that record. This is a local maintenance helper, not a transaction manager or security sandbox. Do not run it concurrently with another installer or editor changing its targets.

`connections` prints only server names, transport and enabled status. It never prints URLs, commands, environment variables or credentials and does not claim runtime availability. The helper does not change MCP configuration. Required provider setup remains a separate authorized native host action.

The optional profiles are `constellation-builder`, `constellation-designer`, `constellation-security` and `constellation-reviewer`; ask the lead to use one for a bounded task when delegation is authorized. They contain only name, description and developer instructions, so model/provider/permissions/MCP follow the parent. Their no-edit instructions are behavioural requests, not read-only enforcement. Runtime selection requires a host exposing custom agent types; otherwise the lead can proceed or disclose explicitly authorized instruction-based delegation. Read the skill's [runtime reference](../.agents/skills/constellation-workflow/references/runtime.md) only when needed.

The package command builds a skills-only private plugin from the same maintained source and `toolkit/plugin.json`. Native local profiles are deliberately separate. Account saving, installation and activation on each surface are separate states; a saved ChatGPT plugin does not install personal agents into ChatGPT. No new server, paid API or hosting is required.

Automatic selection uses the skill description and the host's discovery lifecycle; it is not guaranteed. Open a fresh Codex chat, inspect its available skills and invoke `$constellation-workflow` explicitly. If it is missing, confirm the host's active skills directory and reload/restart as needed. A filesystem copy or validation pass cannot prove session activation.

## Compatibility and scope

This is Constellation's product interaction with an existing Codex host. Reusable engineering/design/security methods remain in their owners. It is distinct from Polaris's repo-local `constellation-a0`, which handles explicit experimental routing/result/evidence contracts. Do not load both by default or treat either as an execution attestation.

Existing governed adopters retain their mandatory readings, planner and approval obligations. Unadopted projects do not inherit them by installing this skill. No adoption configuration, philosophical canon or capability contract changes here. The conditional adoption reference explains the BSDL/Meridian/BSF versus repository naming discrepancy without resolving it by fiat.

The core follows Polaris's Context and Consistency laws (investigate and keep the workflow small), Adaptability (recommend reversible defaults), Human Primacy and AI agency boundaries (retain meaningful product decisions and approvals), Evidence (report actual checks), and Architectural Memory (reuse durable project records).

## Acceptance and evidence

Request `constellation-codex-workflow-001`: deliver a compact conversational entry point with conditional guidance, preserve governance/A0 boundaries, install additively, validate structure and return a reviewable change. No application runtime or build/test toolchain exists in this repository. There is no fitting existing product implementation playbook; skill-creator validation and focused document/package inspection apply.

Reviewed source revisions:

| Source | Revision | Use |
| --- | --- | --- |
| Constellation baseline | `9cbc243` | Product, adoption, charter, roadmap and proposed pilot |
| Polaris | `ed10f82764685526ab69b66db7edab7a998fd0f9` | Constitution, operating rules, composition and A0 distinction |
| Axis | `e1c8581b07b4c462ed9f0c8fab42150454311ef8` | Selected engineering/documentation lens |
| Meridian | `d16ad6136c141a390a9310bf547128b873fc8771` | Compatibility reading; no UI/design change |
| Sentinel | `467d8d9d66b813d54b53e05f327be9467fc861ed` | Compatibility reading; no product trust-boundary change |

The adopted version-1 planner returned `ready`, selected Axis, and reported no coverage gaps. This was planning validation, not execution proof. Meridian and Sentinel were inspected for compatibility; neither was assigned an implementation task. One lead performed this change; no independent review or behavioral execution is claimed.

See [STATUS](../STATUS.md) for checks actually run and remaining validation. Structural validation does not show that future conversations follow the skill, reduce question burden, deliver correct software or satisfy a real adopter. The next real request is the useful behavioral trial; do not mark an A0 pilot or milestone complete from this change.

## Toolkit extension

Request `constellation-toolkit-001` extends the original workflow with optional native profiles and deterministic maintenance. The lead remains accountable; Axis, Meridian, Sentinel and Polaris remain conditional knowledge/review responsibilities, not a compulsory running team. Preserve the terminology boundary described in the adoption reference: this implementation does not redefine BSDL, holistic Meridian or BSF, or amend repository canon.

Installation/update authorization is supplied by the owner’s toolkit execution request. Backup preservation follows Adaptability; one lead and small profiles follow Context and Consistency; honest checks follow Evidence; project-owned continuation follows Architectural Memory. The installer creates no permission boundary. The adopted planner selected Axis and Sentinel with `ready` status, no coverage gaps, at the same source revisions listed above. Meridian was read for profile compatibility, without a product UI/Figma assignment. No existing playbook describes local skill/profile packaging; Skill Creator, Plugin Creator and current official host docs govern the package mechanics.

Official formats verified on 19 October 2026: [native custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [plugin packaging](https://developers.openai.com/plugins/build/plugins), and [documentation MCP](https://developers.openai.com/learn/docs-mcp). See STATUS for execution evidence and remaining gates.

## Evidence-Based Engineering — 20 October 2026

The owner's policy implementation updates the maintained skill and optional profiles. Polaris owns operational adoption in ADR-007 and PROJECT_RULES; Axis owns [the engineering method](https://github.com/pedrobritx/axis/blob/main/guides/evidence-based-engineering.md); Sentinel owns [security evidence](https://github.com/pedrobritx/sentinel/blob/main/guidance/project-context.md). Record reviewed revisions; discovery links are not proof of adoption/merge. The workflow keeps local checkpoints distinct from remote publication, applies local verification and contextual Docker/native environments, and reuses existing records. This does not implement an application runtime or configure CI branch protections. Local installation, account plugin packaging and fresh-session activation remain separate states.
