---
name: task-bootstrap
description: Initialize the active GCC memory tree for a new task.
---

# task-bootstrap Skill

## Purpose
Create a fresh `.ai-governance/docs/task/active/` directory with the GCC structure.
Use this when starting a new task from scratch.

## Instructions

1. **Check if `.ai-governance/docs/task/active/` already exists.**
   - If it exists and has content, ask the user: *"An active task already exists. Do you want to archive it and start a new one, or continue the existing task?"*
   - If archive: run `task-archive` first.
   - If continue: run `task-context` instead.

2. **Create the GCC directory tree**:
   - `.ai-governance/docs/task/active/`
   - `.ai-governance/docs/task/active/branches/main/commits/`

3. **Initialize Core Files**:
   - `task.md` — Ask the user for: Task name, objective, success criteria.
   - `plan.md` — Draft the overall technical approach.
   - `branches/main/summary.md` — Initialize with:
     ```
     # Branch Summary: main
     ## Intent
     [From task objective]
     ## Status
     Just initialized.
     ## Latest Commits
     - none
     ## Next Action
     Start exploration or implementation.
     ```

4. **Confirm**: *"Active GCC task created at .ai-governance/docs/task/active/ on branch `main`. I am ready to start work."*
