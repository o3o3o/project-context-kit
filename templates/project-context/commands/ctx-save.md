---
name: ctx-save
description: Write back the current execution state before ending the session.
---

# /ctx-save

Purpose:
Write back the current execution state before ending the session so the next agent can resume quickly.

## Update logic

1. **Ensure Active Tree Exists**: If `docs/task/active/` or its core files are missing, initialize them before writing.
2. **Extract Knowledge**: If you learned universal project patterns, update `.project-context/docs/project/context.md`.
3. **Promote Decisions If Needed**: If you reached a project-level design conclusion that should outlive the current task, add or update a file in `.project-context/docs/decisions/`.
4. **Sync Project Docs If Needed**:
   - Architecture or module boundaries changed? Update `.project-context/docs/project/architecture.md`.
   - Commands, runtime, repo layout, or branch conventions changed? Update `.project-context/docs/project/metadata.yaml`.
   - Coding style, safety rules, or conventions changed? Update `.project-context/docs/project/coding-standards.md`.
   - Verification order or proof standard changed? Update `.project-context/docs/project/verify-runbook.md`.
5. **Capture Assets**: If you have critical logs or artifacts, move them into `.project-context/docs/task/active/assets/`.
6. **Refresh Fast Index**: Update `.project-context/docs/task/active/index.md`.
7. **Refresh Task State**:
   - Overwrite `.project-context/docs/task/active/summary.md` with current state, completed work, blockers, task-local decisions, and next executable action.
   - Update `.project-context/docs/task/active/verification.md` whenever tests, manual checks, review conclusions, skipped checks, or validation gaps changed materially.
   - Milestone reached? -> Call `activate_skill(name="context-checkpoint")`.
8. **Archive If Complete**:
   - If `.project-context/docs/task/active/verification.md` explicitly says `Status: Complete` or `Status: Done`, archive the current active task snapshot before ending `/ctx-save`.
   - Move `.project-context/docs/task/active/index.md`, `task.md`, `summary.md`, `verification.md`, and any `commits/`, `assets/`, or `workstreams/` into `.project-context/docs/task/archive/YYYY-MM-DD-<slug>/`.
   - Derive `<slug>` from the task title in `task.md`. If no good short name exists, create a short readable slug from the task title.
   - After archiving, recreate `.project-context/docs/task/active/` from `.project-context/docs/task/_template/`.

## Rules

- **Hermeticity**: Ensure all references are internal to `.project-context/`.
- Overwrite the file; do not append logs.
- Keep `active/index.md` short and scannable.
- Use the root task files for the common case.
- Write facts that survive a context reset: what changed, what was verified, what is unknown, and what to do next.
- If a task changes project-level architecture, commands, conventions, or verification policy, update the matching `docs/project/` file before ending `/ctx-save`.
- Do not leave completed-task history in `active/`; move completed task files to `archive/`.
- Archiving is part of `/ctx-save` when the task is explicitly complete, not an optional follow-up step.
- Do not leave long-lived design conclusions only in `summary.md`; promote them into `docs/decisions/`.
