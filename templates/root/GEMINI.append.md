## Project Context (v3.2)
- **Metadata**: @.project-context/docs/project/metadata.yaml
- **Shared Rules**: @.project-context/AGENTS.shared.md
- **Contract**: @.project-context/repo-contract.md
- **Active Task**: @.project-context/docs/task/active/index.md

**Use when needed**: Invoke the project-context agent command `ctx-load` when you need to recover project or task context from durable state. Do not execute it in bash.
**Required on every session end**: Invoke the project-context agent command `ctx-save`. Do not execute it in bash.

`.project-context/` is the durable project memory layer.
