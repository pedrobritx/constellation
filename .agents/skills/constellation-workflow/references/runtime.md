# Native runtime and optional delegation

Use the host's tool loop, permission controls, skill discovery and context handling. Inspect currently exposed tools first; discover the relevant connector only when it serves the next task. Verify a low-impact read before claiming a connection works. Configuration, tool discovery, successful reads and successful writes are different evidence. Never print connection secrets or sensitive endpoints. Use official OpenAI Docs for current host/API behaviour. Add connections only within authorization and concrete need.

One ordinary lead remains accountable. When bounded delegation is authorized and useful, prefer the installed native profiles:

| Profile | Useful assignment |
| --- | --- |
| `constellation-builder` | Implement one agreed slice with clear file/interface ownership |
| `constellation-designer` | Specify/review one interaction and its complete accessible states |
| `constellation-security` | Inspect concrete trust/data/permission boundaries |
| `constellation-reviewer` | Independently inspect the integrated change and evidence |

Give the selected agent the actual objective, acceptance criteria, approved scope, owned artifacts, shared interfaces and only relevant context/revisions. Retain existing request IDs where adopted. Ask for artifacts, actual checks/results, decisions and blockers in a brief useful return. Reconcile changes and directly inspect the integrated result; delegation is not acceptance.

Native profiles are standalone TOML under `~/.codex/agents/` (or the host's active personal agents directory) or project `.codex/agents/`. They inherit parent permissions/provider/MCP/model settings. A profile's no-edit instruction does not enforce a read-only sandbox. If the host cannot select custom profiles, keep the lead responsible; an explicitly authorized generic subagent can receive the bounded instructions, but report that as instruction-based delegation rather than native profile activation. Do not imitate unsupported spawn arguments or claim profiles ran from file validation.

The portable plugin contains this workflow and references. It does not install personal Codex profiles into ChatGPT. Local installation and source consistency are checked by Constellation's `automation/toolkit.py`; a new host session must still discover and activate installed components.
