# Product scope

Constellation is the intended BRITX STUDIO product that brings AI assistance, visual construction and editable code into one software-building workflow. Polaris coordinates; Axis, Meridian and Sentinel contribute independently maintained capabilities. The constituent repositories are not duplicate application implementations.

The first integration boundary is the request/handoff contract owned by Polaris. A human or host AI inspects an adopting project, supplies acceptance criteria, chooses enabled disciplines, performs or delegates the work within host authority, and returns inspectable artifacts plus fresh evidence. The local planner verifies the composition; it is not an autonomous execution service.

## Delivery boundary

Current deliverables are repository ownership, explicit adoption configuration and contribution scope. A future thin application slice should load a project, show its enabled disciplines and request scope, expose a reviewable handoff plan and display evidence/coverage gaps. Visual editing, code generation/execution, credentials, persistence, collaboration and deployment each need a concrete design and implementation decision before they become product claims.

Use the existing project stack when one exists. The owner's TypeScript/Next.js/React preferences can guide a new application decision, but this scope record does not install a framework, backend, cloud provider or paid service. No user-facing application exists yet.

## Acceptance for composition

- Polaris can coordinate a request using reviewed project and constitutional context.
- Axis, Meridian and Sentinel have distinct reusable ownership and explicit handoff outputs.
- Any subset can be selected; missing required sources fail visibly and excluded requested scopes remain unverified.
- Product-specific code/design/security records stay in the product; reusable changes stay in the discipline.
- Plans, implemented behaviour, automated checks and independent observations remain distinguishable.
