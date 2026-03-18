---
name: task-context
description: Load and summarize the current active GCC state (Replaces task-resume).
---

# task-context Skill

## Purpose
Synthesize the current GCC execution state by reading the repository metadata, task files, and the active branch's latest commits.
Use this at the start of every session.

## Instructions

1. **Check for Active Task**:
   - If `.ai-governance/docs/task/active/` does not exist, tell the user: *"No active task found. Please run `task-bootstrap`."* Stop.

2. **Read Structural Metadata**:
   - `.ai-governance/docs/project/metadata.yaml` (Project constraints and paths).

3. **Read Task Definition**:
   - `.ai-governance/docs/task/active/task.md` (The goal).

4. **Identify Active Branch**:
   - Determine which branch in `branches/` you are working on (usually `main`).
   - Read `branches/<active-branch>/summary.md`.
   - Read the 1-2 most recent files in `branches/<active-branch>/commits/`.

5. **Output a structured Context View**:

   ```text
   ## GCC Context View (Branch: <active-branch>)
   
   **Project Env**: [Key constraints from metadata.yaml]
   **Objective**: [From task.md]
   
   **Branch Status**: [From summary.md]
   
   **Latest Commits**:
   - [Summarize the last commit's Changes and Decisions]
   
   **Open Problems / Blockers**: [From summary.md or last commit]
   
   **Next Action**: [What should happen now]
   ```

6. **Ask the user**: *"Shall I proceed with [Next Action]?"*
