---
name: task-archive
description: Archive the current active task and clear docs/task/active/ for a new task.
---

# task-archive Skill

## Purpose
When a task is complete (or is being put on hold), move it from `.ai-governance/docs/task/active/` to
`.ai-governance/docs/task/archive/<name>/` so the workspace is clean for the next task.

## Instructions

1. **Read `.ai-governance/docs/task/active/task.md`** to get the task name.

2. **Ask the user to confirm** the archive name (suggest: `YYYY-MM-DD-<task-slug>`).

3. **Create the archive directory**: `.ai-governance/docs/task/archive/<archive-name>/`

4. **Move all files** from `.ai-governance/docs/task/active/` to `.ai-governance/docs/task/archive/<archive-name>/`.

5. **Write a final summary** to `.ai-governance/docs/task/archive/<archive-name>/handoff.md`:
   - Final status (completed / on hold / cancelled)
   - Brief outcome summary
   - Date archived

6. **Clear `.ai-governance/docs/task/active/`** (delete it or leave it empty).

7. **Confirm** to the user: *"Task archived at .ai-governance/docs/task/archive/<archive-name>/. Active task cleared. Run `task-bootstrap` to start a new task."*

## Constraints
- Never delete the archive — only move files.
- Always write a final handoff.md before moving files.
