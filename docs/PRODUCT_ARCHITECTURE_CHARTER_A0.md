# Constellation — Product & Architecture Charter (A0)

**Status:** Proposed for owner review; 5W2H interview directions, not a constitutional amendment.  
**Owner:** BRITX STUDIO / human project maintainer  
**Goal:** [Constellation A0](https://github.com/pedrobritx/constellation/issues/2)  
**Sources:** [Polaris Constitution](https://github.com/pedrobritx/polaris/tree/main/polaris/constitution) · [Composition draft](https://github.com/pedrobritx/polaris/pull/9)

## Product thesis

Constellation is an adaptive, evidence-driven way for individual developers to build software with AI coding hosts. Its purpose is reliable multidisciplinary coordination—not the automatic multiplication of agents. Initial A0 is a local-first AI engineering framework. The later integrated visual/code workspace (B) and managed software-building platform (C) are separate proposed investments, not A0 dependencies.

## Seven 5W2H decisions

| Question | A0 decision |
| --- | --- |
| What | Host-integrated engineering framework first; visual/code workspace later |
| Why | Reduce cross-disciplinary coordination failures in AI-assisted software development |
| Who | Individual developers and AI coding agents; human remains accountable |
| Where | Existing coding hosts, local Git, optional GitHub shared tracking/evidence |
| When | Readiness on a real G1–G6 end-to-end pilot, never on an invented deadline |
| How | Adaptive orchestration: unified by default, bounded specialists when justified; controlled approvals independently |
| How much | Balanced measurable investment, existing tools first; spending requires human authorization |

## Ownership and independence

- **Constellation:** product definition, roadmap, adoption, evaluations, future workspace and Constellation-specific source.
- **Polaris:** canonical philosophical/operational governance, composition contract, routing, coordination and host adapters.
- **Axis:** independently adoptable engineering/architecture methods, QA, playbooks and optional profiles.
- **Meridian:** independent interface methods, tokens/components, UX and accessibility verification guidance. Stable 0.5 is not replaced by 0.6 Lab.
- **Sentinel:** security review methods, trust-boundary guidance and verification evidence, not a custom authentication provider.
- **Adopting product:** actual source, relevant designs, project decisions, security findings, test results and evidence of implementation.

Polaris governance is explicitly adopted; each specialist capability can work independently. Disabled relevant disciplines are coverage gaps until an alternative responsible process provides evidence. Security and accessibility obligations never disappear through opt-out.

## Operational model

1. **Intake:** inspect repository and authorized scope, context, acceptance criteria and constraints.
2. **Routing:** select concerns independently from agent count; explain why unified, coordinated or parallel strategy fits; use a controlled approval overlay for consequential operations.
3. **Preflight:** validate adopted contracts, source revisions, unavailable context, permission boundaries and gaps. An accepted plan is not completed execution.
4. **Execution:** use an existing approved coding host (Codex first), one agent by default. No self-escalated permissions or unsupported subagent claims.
5. **Reconciliation:** inspect changed interfaces, conflicting recommendations, missing deliverables and affected disciplines.
6. **Verification:** record actual checks, exit status, source revision, limitations, unresolved high/critical issues and independently observed results only where performed.
7. **Documentation and evidence:** update affected docs/ADRs in the adopting project's same reviewable change and retain concise durable outcomes, not secrets or unrestricted transcripts.
8. **Human review:** request consequential approvals, report complete/partial/blocked states; never auto-merge, release, deploy, spend or alter security posture.

### Non-goals for A0

No hosted LLM/agent runtime, new persistent database, visual builder, universal stack migration, compelled telemetry, compulsory use of all disciplines, automatic PR merge/deployment, or public release. A second coding host is M3, not initial A0 scope.

## Functional and quality requirements

- FR-01: Support at least one real AI coding host and existing project conventions.
- FR-02: Inspect project-specific context and record acceptance criteria and uncertainty.
- FR-03: Respect explicit governance/discipline adoption and report uncovered required scope.
- FR-04: Explain routed concerns, execution mode and human approval requirements.
- FR-05: Execute authorized work via host capabilities; never let planning masquerade as implementation.
- FR-06: Preserve verifiable source/discipline revisions, actual check results and limitations.
- FR-07: Update affected documentation and consequential ADRs alongside implementation.
- FR-08: Preserve least-privilege trust boundaries, host approvals and independent review when required.
- FR-09: Maintain offline/local-first operation, stable versioned contract behavior and discipline independence.

## Acceptance milestones

- **M0 – Foundation:** review cross-repository draft PRs, ratify product charter, stabilize versioned contracts, define pilot.
- **M1 – Operational:** host-neutral intake, tested adaptive routing, first Codex workflow, execution state, evidence and docs plus negative tests.
- **M2 – End-to-end pilot / A0 gate:** G1 scope; G2 coordination; G3 functional implementation; G4 real verification; G5 docs/evidence; G6 human acceptance.
- **M3 – Portability:** second coding host, more failure recovery and varied adopters; deferred.
- **M4 – Distribution:** licensing, external onboarding, maintenance policy and explicit public release; deferred.

A single pilot demonstrates *feasibility*, not general reliability or superior performance. Compare equivalent feature tasks against a simpler coding-agent baseline with predetermined evaluation criteria.

## Evidence and costs

Track success against criteria, applicable discipline coverage, unresolved risks, human interventions, elapsed time, measurable model/API usage, CI cost if available, rework and maintenance overhead. Missing measurements are **unknown**, never zero. Spending/production changes require human authorization. Avoid logging credentials or private project data in public repositories.

## Decision state

The Polaris Constitution, its accepted operating rules, ADR-004 and ADR-005 are existing authority. Draft [Polaris #9](https://github.com/pedrobritx/polaris/pull/9) and dependent capability PRs contain implementation candidates, not merged main-branch rules. This document is a product-direction proposal; changes to philosophical canon/hard constraints require separate human ratification. Accepted implementation details must be recorded through reviewable ADRs and evidence.
