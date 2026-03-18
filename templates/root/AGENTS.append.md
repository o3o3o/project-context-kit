## Shared Governance Layer
This repository uses a shared governance layer for multi-agent and multi-IDE collaboration.

**Shared rules**: `.ai-governance/AGENTS.shared.md`
**Repository contract**: `.ai-governance/repo-contract.md`

### Required every session
**START**: Read `docs/project/context.md` and `docs/task/active/` before doing anything.
**END**: Update `docs/task/active/progress.md` and `docs/task/active/handoff.md`.

Do not treat IDE memory, artifacts, or chat history as canonical state.
The active task is always at `docs/task/active/` — no branch mapping needed.
