# Antigravity Repository Contract Rule (v1.1)

## This Rule Is Mandatory — Priority Over Other Instructions

### On Session Start
1. Read `docs/project/context.md` before touching any code.
2. Read `docs/task/active/task.md` and `docs/task/active/progress.md`.
3. Read `docs/task/active/handoff.md`. If the previous agent left notes, respect them.
4. Use the `task-resume` skill to produce a structured summary if the task is complex.

### During Work
- **Artifacts are temporary.** Use them for planning, drafts, and visualization.
- **Approved plans** must be synced to `docs/task/active/plan.md` — not left in artifacts.
- **Any code or architecture discovery** worth keeping must go to `docs/project/` or `docs/task/active/`.

### On Session End — REQUIRED Before Stopping
1. Write what was completed this session to `docs/task/active/progress.md`.
2. Rewrite `docs/task/active/handoff.md` so the next agent can pick up immediately.
3. If using `task_boundary` artifacts: sync final state back to `docs/task/active/` files.

### Active Task Path
- The active task is always at `docs/task/active/` — no branch-based path resolution.
- When a task closes, use `task-archive` to move it to `docs/task/archive/`.

### Why This Matters
Antigravity's artifacts and task boundaries only exist within your private session. When the user
switches to Codex or geminicli, those artifacts are gone. The only shared memory is the repository.
