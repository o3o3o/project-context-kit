# Verification Runbook

## Verification Hierarchy
Before declaring a task finished, choose the smallest check that proves the changed surface, then widen only when risk requires it.

1. **Focused Check**: Run the narrow test, lint, build, script, or manual check that covers the changed files.
2. **Integration Check**: Verify connected components when the change crosses module boundaries.
3. **Build / Package Check**: Run when installable artifacts, generated files, or deployment paths changed.
4. **Manual Check**: Use for UI/API/user workflow changes where automated proof is incomplete.
5. **Full Check**: Run the full suite only when the change is broad or the focused result is insufficient.

## Recording Results
Record the latest durable result in `.project-context/docs/task/active/verification.md`.

Each meaningful check should record:

- Command or manual check
- Result: Passed, Failed, Skipped, or Not run
- Date
- Environment
- Notes or failure reason
- Remaining validation gap

## Minimum Standard
- Do not mark a task complete unless success criteria and verification agree.
- If the task changed architecture, commands, conventions, or verification policy, the matching `.project-context/docs/project/` file must be updated or the gap must be recorded in `verification.md`.
- If verification is skipped, record why and what risk remains.
- If a check fails for unrelated reasons, record the failure and the reason it is treated as unrelated.
- Large logs belong in `.project-context/docs/task/active/assets/`; summaries belong in `verification.md`.
