## Project Context (v3.2)
- **Execution Metadata**: .project-context/docs/project/metadata.yaml
- **Active Task View**: Use the project-context agent command `ctx-load` when you need to recover durable task state. Do not execute it in bash.
- **Shared Rules**: `.project-context/AGENTS.shared.md`
- **Contract**: `.project-context/repo-contract.md`

### Session Lifecycle
**LOAD WHEN NEEDED**: Invoke the project-context agent command `ctx-load` when task context, project state, or handoff details need to be reconstructed. Do not execute it in bash.
**END**: Invoke the project-context agent command `ctx-save` before ending the session. Do not execute it in bash.

Default mode uses the active task files in `.project-context/docs/task/active/`. `.project-context/` is the durable project memory layer. Git records the "What"; Project Context records the resumable "Why" and "What next".
