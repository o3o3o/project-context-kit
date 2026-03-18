## Shared Governance Layer (GCC Model)
This repository uses a Git-Context-Controller (GCC) shared governance layer for multi-agent collaboration.

**Shared rules**: `.ai-governance/AGENTS.shared.md`
**Repository contract**: `.ai-governance/repo-contract.md`

### Required every session
**START**: Read `.ai-governance/docs/project/metadata.yaml` and `.ai-governance/docs/task/active/task.md`. Check active branch (`summary.md` and `commits/`).
**END**: Execute a commit into the active branch's `commits/` dir and update `summary.md`.

Do not treat IDE memory, artifacts, or chat history as canonical state. All context is built from the GCC tree.
