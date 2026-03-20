---
name: task-commit
description: Create a structured project-context checkpoint (v3.2).
---

# task-commit Skill

## Purpose
Serialize current progress, reasoning, and decisions into the GCC history. Use this when a meaningful milestone is achieved.

## Instructions

1. **Verify Mandatory Fields**: Your commit MUST include:
   - **Intent**: What did you set out to solve?
   - **Previous Context**: What state did you start from?
   - **Changes Made**: Specific files and logic changes.
   - **Decisions**: **WHY** did you choose this path? (Critical for cross-agent alignment).
   - **Verification**: Evidence (test output, logs).

2. **Generate Commit**:
   - Default target: `docs/task/active/commits/YYYY-MM-DD-HHMM-[slug].md`.
   - Optional advanced target: `docs/task/active/workstreams/<name>/commits/YYYY-MM-DD-HHMM-[slug].md`.

3. **Update Summary**:
   - Update `docs/task/active/summary.md` by default.
   - Refresh `docs/task/active/index.md` with the latest milestone and next step.
   - If operating inside a named workstream, update that workstream summary as well.

4. **Final Check**: Ensure you didn't just summarize code; summarize the **cognitive decisions** that influenced the code.
