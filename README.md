# Constellation

A planned hybrid software-building product combining AI assistance, visual construction and editable code under BRITX STUDIO. This repository owns the product definition and future application. Its current contents establish that scope; they do not implement a builder or autonomous execution service.

Requests normally enter through **[Polaris](https://github.com/pedrobritx/polaris)**, which reads project context and its Constitution, selects appropriate disciplines, coordinates handoffs and checks the integrated result.

| Capability | Independent repository |
|---|---|
| Governance, request analysis and orchestration contracts | [Polaris](https://github.com/pedrobritx/polaris) |
| Architecture and engineering | [Axis](https://github.com/pedrobritx/axis) |
| Interface design and accessibility methods | [Meridian](https://github.com/pedrobritx/meridian) |
| Security engineering and review | [Sentinel](https://github.com/pedrobritx/sentinel) |

Each discipline remains independently usable. [constellation.json](constellation.json) records this product's adoption choices. Disable a discipline explicitly with a reason; arrange alternative coverage for affected requirements. Governance adoption is separate from discipline adoption. The shared [composition contract](https://github.com/pedrobritx/polaris/blob/main/integration/README.md) owns the protocol; this product does not fork it.

For the implemented Codex-first entry point, see [the lightweight workflow](docs/codex-workflow.md). It includes optional native profiles, an installer/verifier and a private skills-only package, supporting conversation and authorized delivery in an existing Codex host; the planned hybrid application remains future scope.

Start with [AGENTS.md](AGENTS.md) and [product scope](docs/product.md). Product source, UX, decisions and execution evidence belong here. Reusable methods, shared design components and security review guidance belong in their owning repositories.
