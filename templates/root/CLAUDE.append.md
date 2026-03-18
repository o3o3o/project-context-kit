## Shared Governance (GCC Model v2.1)
- **Execution Metadata**: .ai-governance/docs/project/metadata.yaml
- **Active Task View**: Run `task-context`

Follow: `.ai-governance/CLAUDE.shared.md`

### Session Lifecycle
**START**: Load `metadata.yaml`, `task.md`, and the current branch `summary.md`.
**END**: `task-commit` for successful milestones; otherwise, update `summary.md` (Current State/Next Action).

GCC records our "Why" (decisions). Git records the "What" (code).
