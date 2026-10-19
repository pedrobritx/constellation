# Lightweight Constellation workflow in Codex

The first usable slice is a normal skill: [constellation-workflow](../.agents/skills/constellation-workflow/SKILL.md). Invoke `$constellation-workflow` with an idea, existing project request or request to resume. Codex investigates, recommends, discusses consequential choices, builds authorized work and leaves project-owned continuity. No standalone app, paid provider, service or pilot selection is required.

## Installation and discovery

The maintained source is `.agents/skills/constellation-workflow/`. Repo-local discovery applies in a Codex session that discovers this repository's skills; this folder alone is not globally available in unrelated projects.

For cross-project use, copy that directory additively to `${CODEX_HOME:-$HOME/.codex}/skills/constellation-workflow` only if the destination does not exist. Preserve all three files and do not overwrite another installation. Updates need an explicitly reviewed replacement; this slice supplies no updater or global configuration change. The local installation made during this task is recorded in [STATUS](../STATUS.md).

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
