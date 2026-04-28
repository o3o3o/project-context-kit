# Active Task Templates

This template set supports a simple harness workflow: one active task, one optional module list, and explicit verification evidence.

## Minimal Flow
1. Run `context-bootstrap` or copy the active task templates into `docs/task/active/`.
2. Fill in `index.md` and `task.md` for the main task.
3. If the task can be split, list assignable modules in `tasklist.md`.
4. Keep at most one module `In Progress` per agent unless the user explicitly asks for parallel work.
5. When a module is claimed, update `Status`, `Owner`, `Branch`, `Last Update`, and `Notes`.
6. When a module is done, record the verification evidence in `tasklist.md` and update `verification.md`.

## Rules
- Keep the main chain in `active/task.md`.
- Use `tasklist.md` only for modules that are safe to assign separately.
- Do not create per-module document trees by default.
- Do not mark a module `Done` without verification evidence.
- Keep all references hermetic inside `.project-context/`.
