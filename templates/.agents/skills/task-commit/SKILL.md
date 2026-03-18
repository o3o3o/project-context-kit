---
name: task-commit
description: Create a structured commit file to serialize cognition and progress.
---

# task-commit Skill

## Purpose
In the GCC model, we do not continuously append to a linear log. We create distinct "commits" to summarize reasoning, changes, and next steps for the incoming agent. Use this before ending a session.

## Instructions

1. **Determine Active Branch**: Ask the user or infer from `task-context` which branch you are on.
2. **Generate Commit ID**: Use the format `YYYY-MM-DD-HHMM-xxx.md` (e.g., `2026-03-18-1030-auth-fix.md`).
3. **Write the Commit File**:
   Create the file in `.ai-governance/docs/task/active/branches/<branch>/commits/<id>.md`.
   Use this template:
   ```markdown
   # Commit: <id>
   ## Intent
   [What problem were you solving in this session?]
   ## Changes Made
   [List modified files and core logic changes]
   ## Decisions
   [Why did you choose this approach?]
   ## Risks / Next Steps
   [What is pending or might break?]
   ```
4. **Update Branch Summary**:
   Rewrite `.ai-governance/docs/task/active/branches/<branch>/summary.md` to update the active status, append the `<id>` to the "Latest Commits" list, and update the "Next Action".
5. **Confirm**: *"Commit `<id>` created on branch `<branch>`. Summary updated."*
