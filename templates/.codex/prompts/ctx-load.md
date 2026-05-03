---
name: ctx-load
description: Reconstruct durable project and task context when `/ctx-load` is explicitly invoked.
---

# /ctx-load

Purpose:
Reconstruct durable project and task context from repo-native project-context files when `/ctx-load` is explicitly invoked.

## Read in order

1. `.project-context/runtime/context-map.yaml` if present and fresh
2. `.project-context/docs/task/active/index.md` if the map is missing, stale, or has placeholder `current` fields
3. `.project-context/docs/task/active/summary.md` for the current state snapshot
4. `.project-context/docs/project/metadata.yaml` (Env & Commands), when needed
5. `.project-context/docs/project/context.md` (Architecture & History), when needed
6. `.project-context/docs/decisions/` (Long-lived design choices, if relevant)

## Expand only if needed

7. `.project-context/docs/task/active/task.md` (Goal)
8. `.project-context/docs/task/active/tasklist.md` only when claiming module work, checking active/blocked module detail, or global scheduling
9. `.project-context/docs/task/active/verification.md` (Latest validation state)
10. `.project-context/docs/task/active/commits/` (Recent milestone context, if present)

## Rules

- **Gemini CLI / Antigravity**: Call `activate_skill(name="context-load")` after reading these files to synthesize the session brief.
- `.project-context/runtime/context-map.yaml` is a generated routing cache, not the source of truth. Do not edit it manually.
- Reconstruct these six facts before acting: project constraints, active objective, current repo state, active module ownership if any, latest verification, and next executable action.
- Prefer `active/index.md` and `summary.md` as the fast state view.
- Read `docs/decisions/` only when the current task depends on earlier project-level decisions.
- Treat `docs/task/archive/` as history, not startup context. Only read archived tasks when the user explicitly asks for historical context.
- If the active task files are missing, initialize them from `.project-context/docs/task/_template/` or offer to run `activate_skill(name="context-bootstrap")`.
- If recent milestone commits exist, read the latest 1-2 before acting.
- Do not read `tasklist.md` by default.
- Keep output brief and execution-oriented. Do not produce a task diary.
