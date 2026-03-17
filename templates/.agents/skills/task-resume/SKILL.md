---
name: task-resume
description: Read the current task state from the repository and summarize it.
---

# task-resume Skill

## Purpose
Provide a concise summary of the active task state by reading the canonical files in the repository, ensuring the agent is fully synced with the work done by previous agents.

## Instructions
1. Identify the active ticket ID from the current Git branch.
2. Locate the task directory: `docs/task/<ticket-id>/`.
3. Read the following files:
   - `docs/project/context.md`: For overall project grounding.
   - `docs/task/<ticket-id>/task.md`: For task definition.
   - `docs/task/<ticket-id>/progress.md`: For what has been done.
   - `docs/task/<ticket-id>/handoff.md`: For the last status and next steps.
4. Output a summary to the user including:
   - **Task Objective**
   - **Current Status** (Completed vs. Remaining)
   - **Last Handoff Notes**
   - **Next Action Items**

## Constraints
- If the directory does not exist, suggest running `task-bootstrap`.
