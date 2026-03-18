# AI Agent Instructions

<!-- BEGIN AI-GOVERNANCE -->
## Shared Governance Layer
This repository uses a shared governance layer for multi-agent and multi-IDE collaboration.

**Shared rules**: `.ai-governance/AGENTS.shared.md`
**Repository contract**: `.ai-governance/repo-contract.md`

### Required every session
**START**: Read `.ai-governance/docs/project/context.md` and `.ai-governance/docs/task/active/` before doing anything.
**END**: Update `.ai-governance/docs/task/active/progress.md` and `.ai-governance/docs/task/active/handoff.md`.

Do not treat IDE memory, artifacts, or chat history as canonical state.
The active task is always at `.ai-governance/docs/task/active/` — no branch mapping needed.
<!-- END AI-GOVERNANCE -->
