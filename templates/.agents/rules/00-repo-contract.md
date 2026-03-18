# Antigravity Repository Contract Rule (v2.0 - GCC Model)

## This Rule Is Mandatory — Priority Over Other Instructions

### On Session Start
1. Read `.ai-governance/docs/project/metadata.yaml` for execution constraints.
2. Read `.ai-governance/docs/task/active/task.md` and then view the active branch's `summary.md` and recent `commits/`.
3. You can run the `task-context` skill to automate building the view.

### During Work (Branches)
- **Artifacts are temporary.** Use them for planning, drafts, and visualization.
- If you are trying a complex new approach, **create a new GCC branch** in `.ai-governance/docs/task/active/branches/`.
- Do not pollute the `main` branch with failed experiments.

### On Session End — REQUIRED Before Stopping (Commits)
1. **Never use progress.md**. We use structured commits.
2. Execute a commit into the active branch's `commits/` directory and update the branch's `summary.md`.
3. Next agents will read your commit to know what you discovered or changed.

### Why This Matters
Antigravity's artifacts and task boundaries only exist within your private session. To share state with Codex or geminicli, you must serialize your cognition into the GCC tree.
