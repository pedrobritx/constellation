# A0 pilot candidate — VIA accessible local summary sharing

**Status:** Proposed pilot specification only; no adopter code change or pilot execution.  
**Owner:** Constellation product maintainer (pilot coordination); VIA owns feature implementation.  
**A0 tracking:** [Goal](https://github.com/pedrobritx/constellation/issues/2) · [Pilot definition A0-004](https://github.com/pedrobritx/constellation/issues/4) · [Real pilot A0-013](https://github.com/pedrobritx/constellation/issues/5).  
**Target baseline:** [VIA at commit `2c32a58ba9ab07771991d94bc8554353bc74b900`](https://github.com/pedrobritx/via/tree/2c32a58ba9ab07771991d94bc8554353bc74b900). Reconfirm this baseline when the pilot actually begins.

## Why this project?

VIA already has a real React/Next.js application, deterministic calculations, an existing results view, export-to-JSON/CSV, a human-readable result summary and meaningful accessibility/privacy constraints. Its domain code stays separate from React/Next. The README and `AGENTS.md` explicitly require source-backed calculations, localization and WCAG 2.2 AA. The existing local/offline fallback avoids committing to new third-party credentials or services.

This pilot tests Constellation's ability to preserve existing product-specific commitments instead of imposing a generic default stack or duplicate UI. This is a candidate; **no claim that VIA has adopted the A0 pilot or that the product feature is implemented**.

## One bounded product feature

**Add an explicitly triggered “Copy summary” action to VIA's calculated-results area**, next to its existing JSON/CSV downloads. The clipboard copy must contain an accessible, human-readable, locally generated summary of the current *non-stale* impact result, its `indexVersion` and the meaningful methodological/feasibility caveat already represented by the result. Do not copy exact origin/destination addresses, patient age, mobility or income by default. Do not modify mathematical formulas or `INDEX_VERSION`.

### Why it needs three discipline perspectives

| Concern | Expected contribution |
| --- | --- |
| Axis | Preserve `src/domain/` separation, reuse `buildSummary` and existing result/export APIs, avoid new dependencies, add unit/component tests and deterministic output |
| Meridian | Clear placement, keyboard operability, visible focus, screen-reader `aria-live` success/failure feedback, PT-BR/EN-US catalog strings, no incorrect implication of measured certainty |
| Sentinel | Clipboard is explicit user-initiated disclosure; no silent upload, remote service, analytics or default inclusion of personal or location data; disclose that copies can be read by external apps |

The execution host must follow VIA's own `AGENTS.md`, relevant role files, local i18n conventions and Next.js version-specific documentation before editing.

## Acceptance criteria (pre-registered before either workflow)

1. Given a computed, current result, a keyboard user can activate an explicitly labelled Copy summary action; the copied text reflects the displayed result's semantic summary and includes `indexVersion`.
2. The copied text preserves remote-viability wording and the relevant caveat rather than declaring teleconsultation feasible when the result says it is not.
3. There is no automatic clipboard write, download, network transmission, external service request or analytics emission from this feature; copying requires an intentional action.
4. No address, income, age, mobility profile or other raw sensitive input is copied by default.
5. Clipboard success/failure is available as visible text and announced accessibly; failed permission/API cases never claim success. Focus remains usable.
6. New visible messages are localized through VIA's message catalogs with appropriate fallback behavior; domain logic and deterministic indices are unchanged.
7. Existing JSON/CSV export behavior remains intact and relevant tests cover both success and failure paths, including feasibility and privacy constraints.
8. All four VIA-mandated checks are run in the actual adopter checkout: `npm run test && npm run typecheck && npm run lint && npm run build`. Report exact actual outcomes; do not fabricate test runs.
9. Documentation and relevant decision notes are updated together with the adopter implementation, clearly separating the existing formula from the new user-triggered copy behavior.
10. No production deployment, public release, spending, authentication/security posture adjustment, or unsolicited processing of real patient data.

## Experiment and baseline

- **Control:** an ordinary authorized coding-agent workflow that follows VIA's existing `AGENTS.md` but does not use Polaris routing/structured specialist handoffs.
- **Treatment:** same host, source commit, acceptance criteria and explicit resource permissions, with Polaris A0 intake → route → discipline guidance → authorized implementation → test evidence → documentation.
- **Isolation:** independent branches/worktrees (or equivalent clean resets) on fixed baseline, synthetic input fixtures only, no production credentials.
- **Controls:** same model/provider and resource envelope where possible. If unequal, disclose the difference. Do not intentionally hide relevant safety rules from the control baseline.
- **Pre-registered metrics:** applicable functional and accessibility criteria passed; privacy concerns detected and addressed; number of human interventions; actual elapsed time; recorded model/tool usage if available; rework; resulting docs accuracy. Missing measures are unknown, never zero.
- **Evaluator:** owner inspects both resulting diffs and direct app behavior. A single individual conducting both assessments is **not** described as independent accessibility evidence.

## Evidence gates

- **G1 Context:** immutable source SHA, instructions read, scope, acceptance, risk and permission limitations.
- **G2 Coordination:** documented selection of Axis, Meridian and Sentinel concerns, execution mode and justified handoffs; integrated decisions verified.
- **G3 Functionality:** actual behavior passes mandatory criteria using synthetic fixtures.
- **G4 Verification:** real logs and exit statuses; access/a11y limitations and unresolved risks reported, no unsupported pass.
- **G5 Documents:** source-matched proof of docs/ADR changes and concise evidence ledger; no secrets or unnecessary patient details.
- **G6 Human:** owner accepts/rejects based on product behavior and recorded limitations.

## Exit criteria and prerequisites

A0 cannot claim this pilot complete until Polaris M1 contracts and a real authorized coding host execute and verify the *actual* adopter change. A passing planner/test fixture is insufficient. The project maintainer must review the bounded feature scope before the real product implementation is merged. Any spending, publishing, provider configuration, or production auth change requires separate explicit authorization.

## Deferred

No new export file format, backend, provider, medical recommendation, clinical decision-support claim, analytics, collaboration or hosted worker. No design-system migration to experimental Meridian 0.6. Pilot output remains in VIA; only generalized learning belongs in a discipline.
