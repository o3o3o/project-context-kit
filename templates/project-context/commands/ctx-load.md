---
name: ctx-load
description: Restore the current working context for a new agent session.
---

# /ctx-load

Purpose:
Restore the current working context for a new agent session from repo-native project-context files.

## Read in order

1. `.project-context/docs/project/metadata.yaml` (Env & Commands)
2. `.project-context/docs/project/context.md` (Architecture & History)
3. `.project-context/docs/decisions/` (Long-lived design choices, if relevant)
4. `.project-context/docs/task/active/index.md` (Fast status view)

## Expand only if needed

5. `.project-context/docs/task/active/task.md` (Goal)
6. `.project-context/docs/task/active/summary.md` (Progress)
7. `.project-context/docs/task/active/verification.md` (Latest validation state)
8. `.project-context/docs/task/active/commits/` (Recent milestone context, if present)

## Rules

- **Gemini CLI / Antigravity**: Call `activate_skill(name="context-load")` after reading these files to synthesize the session brief.
- Prefer `active/index.md` as the source of truth for which tasks are currently in progress.
- Read `docs/decisions/` only when the current task depends on earlier project-level decisions.
- Treat `docs/task/archive/` as history, not startup context. Only read archived tasks when the user explicitly asks for historical context.
- If the active task files are missing, initialize them from `.project-context/docs/task/_template/` or offer to run `activate_skill(name="context-bootstrap")`.
- If recent milestone commits exist, read the latest 1-2 before acting.
- Keep output brief and execution-oriented.
