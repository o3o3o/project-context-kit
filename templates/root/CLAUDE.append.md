## Project Context (v3.2)
- **Execution Metadata**: .project-context/docs/project/metadata.yaml
- **Active Task View**: Invoke the project-context agent command `ctx-load`. Do not execute it in bash.

Follow: `.project-context/CLAUDE.shared.md`

### Session Lifecycle
**START**: Invoke the project-context agent command `ctx-load` immediately. Do not execute it in bash.
**END**: Invoke the project-context agent command `ctx-save` before ending the session. Do not execute it in bash.

Default mode uses the active task files in `.project-context/docs/task/active/`. Git records the "What"; Project Context records the resumable "Why" and "What next".
