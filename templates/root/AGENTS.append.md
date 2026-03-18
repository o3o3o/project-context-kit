## Shared Governance Layer (GCC Model v2.1)
This repository uses a Git-Context-Controller (GCC) shared governance layer.

**Rules**: `.ai-governance/AGENTS.shared.md` | **Contract**: `.ai-governance/repo-contract.md`

### Required Every Session
**START**: Read `metadata.yaml` (env/commands) and `task.md`. Run `task-context` to load the active branch state.
**END**: Run `task-commit` for milestones, OR update `summary.md` (State/Next Action) for partial progress.

GCC records context/decisions in `.ai-governance/docs/`. Do not treat IDE memory or chat history as durable state.
