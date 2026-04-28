---
name: context-bootstrap
description: Initialize the Project Context structure (v3.2).
---

# context-bootstrap Skill

## Purpose
Initialize a new active task tree using the Project Context v3.2 schema.

## Instructions

1. **Check Metadata**: Ensure `.project-context/docs/project/metadata.yaml` exists. If not, draft one based on the current repo structure and ask the user to verify.

2. **Create Tree**:
   - `.project-context/docs/task/active/`
   - `.project-context/docs/task/active/index.md`
   - `.project-context/docs/task/active/task.md`
   - `.project-context/docs/task/active/tasklist.md`
   - `.project-context/docs/task/active/summary.md`
   - `.project-context/docs/task/active/verification.md`
   - `.project-context/docs/task/active/commits/`
   - `.project-context/docs/task/active/assets/`

3. **Initialize Summary**: Ensure `summary.md` has:
   - Current State: "Initialized"
   - Known Risks: "None"
   - Next Action: "Drafting implementation plan"

4. **Initialize Index**: Ensure `index.md` contains:
   - Current Goal
   - Current Status: "Initialized"
   - Mainline Boundaries
   - Assignable Modules
   - Next Step: "Drafting implementation plan"
   - Latest Verification: "Not run yet"
   - Latest Milestone: "None yet"

5. **Initialize Task Split Surface**:
   - Ensure `task.md` includes mainline boundaries, delegation policy, and a reference to `tasklist.md`
   - Ensure `tasklist.md` exists as the module registry for manual assignment and WIP control
   - Leave `tasklist.md` minimal if the user does not want decomposition yet
   - Do not create extra per-module task directories by default

6. **Compatibility Note**: Older `branches/main/summary.md` structures may still exist in previously installed repos, but do not create them in new installs.

7. **Ask for Objective**: Prompt the user for the `task.md` contents.
