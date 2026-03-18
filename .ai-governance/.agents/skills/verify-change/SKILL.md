---
name: verify-change
description: Execute verification steps and record results in the repository.
---

# verify-change Skill

## Purpose
Ensure all changes are validated against the project's standards and that evidence of this validation is persisted in the repository.

## Instructions
1. Read `docs/project/verify-runbook.md` to understand the required verification steps.
2. Execute the verification steps (e.g., run tests, build the project, manual checks).
3. Record the results in `docs/task/<ticket-id>/verification.md`.
4. The record must include:
   - **Timestamp**
   - **Command run** (if applicable)
   - **Outcome** (Pass/Fail)
   - **Evidence** (Logs, screenshots, or summaries)
5. Update `docs/task/<ticket-id>/handoff.md` to reflect the verification status.

## Constraints
- Do not skip verification steps unless explicitly authorized.
- Evidence must be clear enough for another agent to trust the result.
