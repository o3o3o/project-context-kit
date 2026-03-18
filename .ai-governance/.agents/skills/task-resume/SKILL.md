---
name: task-resume
description: Load and summarize the current active task from the repository.
---

# task-resume Skill

## Purpose
Sync yourself with the current active task state by reading the repository files.
Use this at the start of every session.

## Instructions

1. **Check if `.ai-governance/docs/task/active/` exists.**
   - If it does NOT exist, tell the user: *"No active task found. Please create one with `task-bootstrap`."*
   - Then stop.

2. **Read these files in order:**
   - `.ai-governance/docs/project/context.md` — project background
   - `.ai-governance/docs/task/active/task.md` — task definition
   - `.ai-governance/docs/task/active/progress.md` — what has been done
   - `.ai-governance/docs/task/active/handoff.md` — what the previous agent left for you

3. **Output a summary** in this format:

   ```
   ## Active Task Summary
   **Task**: [task name from task.md]
   **Objective**: [objective from task.md]

   **Completed so far**:
   - [bullet points from progress.md]

   **Last handoff notes**:
   [key content from handoff.md]

   **Next action**: [what should happen next]
   ```

4. Ask the user: *"Want me to continue with [next action]?"*

## Constraints
- Read from files, not from conversation history.
- If any file is missing, name it specifically and ask the user to create it.
