
## Shared Governance Layer
This repository uses a shared governance layer for multi-agent and multi-IDE collaboration.
Please refer to the following for system-wide rules and project memory:

- **Shared Rules**: [.ai-governance/AGENTS.shared.md](file://./.ai-governance/AGENTS.shared.md)
- **Repository Contract**: [.ai-governance/repo-contract.md](file://./.ai-governance/repo-contract.md)

### Canonical Durable State
Do not rely on private session memory, chat history, or IDE-specific artifacts as the source of truth. All critical project state must be persisted here:

1. **Project Memory**: [docs/project/](file://./docs/project/)
2. **Task State**: [docs/task/](file://./docs/task/) (Mapped by branch name to ticket ID)

Before starting work, always run the `task-resume` skill or read the latest `progress.md` in the active task directory.
