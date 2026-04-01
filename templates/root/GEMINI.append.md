## Project Context (v3.2)
- **Metadata**: @.project-context/docs/project/metadata.yaml
- **Rules**: @.agents/rules/00-repo-contract.md
- **Shared Rules**: @.project-context/GEMINI.shared.md

**Use when needed**: Invoke the project-context agent command `ctx-load` when you need to recover project or task context from durable state. Do not execute it in bash.
**Required on every session end**: Invoke the project-context agent command `ctx-save`. Do not execute it in bash.
