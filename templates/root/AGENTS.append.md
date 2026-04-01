## Project Context Layer (v3.2)
This repository uses a Project Context shared context layer.

**Rules**: `.project-context/AGENTS.shared.md` | **Contract**: `.project-context/repo-contract.md`

### Session Guidance
**LOAD WHEN NEEDED**: Invoke the project-context agent command `ctx-load` when you need to recover current task state, durable context, or a clean handoff. Do not execute it in bash.
**END**: Invoke the project-context agent command `ctx-save` to leave a resumable summary for the next agent. Do not execute it in bash.

Default mode uses a single active task in `.project-context/docs/task/active/`. Optional workstreams are advanced mode only.
