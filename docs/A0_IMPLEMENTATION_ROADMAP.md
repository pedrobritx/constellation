# Constellation A0 — Implementation and work tracking

**Cross-repository goal:** [Constellation A0](https://github.com/pedrobritx/constellation/issues/2). **Status:** active implementation; no public release.

| Milestone | Definition of done | Tracking |
| --- | --- | --- |
| M0 – Foundation | Approved compatibility/ownership review, valid standalone manifests, versioned plan, pilot contract | [Review](https://github.com/pedrobritx/polaris/issues/10), [Charter](https://github.com/pedrobritx/constellation/issues/3), [Contracts](https://github.com/pedrobritx/polaris/issues/11), [Pilot design](https://github.com/pedrobritx/constellation/issues/4) |
| M1 – Coordination | Authenticated host-authorized request→execution→check evidence workflow; blocked path correctly fails | [Intake](https://github.com/pedrobritx/polaris/issues/12), [Router](https://github.com/pedrobritx/polaris/issues/13), [Host](https://github.com/pedrobritx/polaris/issues/14), [States](https://github.com/pedrobritx/polaris/issues/15), [Evidence](https://github.com/pedrobritx/polaris/issues/16), [Docs](https://github.com/pedrobritx/polaris/issues/17), [Security](https://github.com/pedrobritx/sentinel/issues/4), [CI](https://github.com/pedrobritx/polaris/issues/18) |
| M2 – Pilot | G1–G6 accepted by human with a real adopter, source revisions, verification and evidence | [Pilot](https://github.com/pedrobritx/constellation/issues/5), [Compare](https://github.com/pedrobritx/constellation/issues/6), [Review](https://github.com/pedrobritx/constellation/issues/7) |
| M3 – Portability | Conformance on another host, more adopters and failure modes | Deferred; requires new scope |
| M4 – Preview | Licensing, onboarding and human-approved publication | Deferred; requires release decision |

## Gate semantics

Planning, execution, verification and approval are separate states. An enabled capability may be unrequested; a requested disabled capability creates an unverified coverage gap. A changed implementation revision invalidates stale evidence. Tests must be real observations, not descriptions. Do not close milestone M2 until human owner accepts the integrated pilot.

## Existing branches

[Polaris #9](https://github.com/pedrobritx/polaris/pull/9) and [Axis #3](https://github.com/pedrobritx/axis/pull/3), [Meridian #37](https://github.com/pedrobritx/meridian/pull/37), [Sentinel #3](https://github.com/pedrobritx/sentinel/pull/3) and [Constellation #1](https://github.com/pedrobritx/constellation/pull/1) must be reconciled before their content is treated as merged canon. Sentinel #2 overlaps #3.

## Safe review sequence

Verify destination discipline manifests and tests first; resolve Sentinel #2/#3; review and merge owning capability changes when authorized; then review Polaris composition and Constellation product definition. This document is not permission to merge, release or deploy.
