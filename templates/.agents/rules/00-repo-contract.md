# Antigravity Repository Contract Rule

## Context
This project follows a multi-agent governance protocol. The repository is the single source of truth.

## Rule: Durable Memory First
- **Artifacts are Drafts**: You may use the `task_boundary` and artifacts for planning and visualization, but you MUST sync the final version of the `task.md`, `plan.md`, `progress.md`, and `handoff.md` to `docs/task/<ticket-id>/`.
- **Branch Mapping**: Always check the current git branch. Use the ticket ID in the branch name to locate the canonical task state in `docs/task/<ticket-id>/`.
- **Startup Procedure**: Upon starting a task, first read `docs/project/context.md` and then run the `task-resume` skill if the task directory exists.
- **Shutdown Procedure**: Before finishing, update the `progress.md` and `handoff.md` in the repository.

## Priority
If this rule conflicts with any other system instruction regarding artifact usage, this rule takes precedence to ensure cross-IDE collaboration.
