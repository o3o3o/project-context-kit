---
name: ctx-save
description: Write back the current execution state before ending the session.
---

# /ctx-save

Purpose:
Write back the current execution state before ending the session so the next agent can resume quickly.

## Update logic

1. **Extract Knowledge**: If you learned universal project patterns, update `.project-context/docs/project/context.md`.
2. **Capture Assets**: If you have critical logs or artifacts, move them to `.project-context/docs/task/active/assets/`.
3. **Refresh Fast Index**: Update `.project-context/docs/task/active/index.md`.
4. **Refresh Task State**:
   - Overwrite `.project-context/docs/task/active/summary.md`.
   - Update `.project-context/docs/task/active/verification.md` whenever validation changed materially.
   - Milestone reached -> Call `activate_skill(name="context-checkpoint")`.
5. **Archive If Complete**:
   - If `.project-context/docs/task/active/verification.md` explicitly says `Status: Complete` or `Status: Done`, archive the current active task snapshot before ending `/ctx-save`.
   - Move `.project-context/docs/task/active/index.md`, `task.md`, `tasklist.md`, `summary.md`, `verification.md`, and any `commits/` or `assets/` into `.project-context/docs/task/archive/YYYY-MM-DD-<slug>/`.
   - After archiving, recreate `.project-context/docs/task/active/` from `.project-context/docs/task/_template/`.

## Rules

- Ensure all references are internal to `.project-context/`.
- Overwrite the file; do not append logs.
- Do not leave completed-task content in `.project-context/docs/task/active/`.
- Do not treat archiving as optional prose; when the task is explicitly complete, move it to `archive/`.
