# Antigravity Repository Contract Rule (v2.1 - GCC Model)

## MANDATORY: Priority Instructions

### GCC Hierarchy & Metadata
- **Use the context map first**: Read `.project-context/runtime/context-map.yaml` first when restoring task state. If you need build commands or directory structure, follow its route to `.project-context/docs/project/metadata.yaml` instead of guessing.
- **Cognitive Isolation**: Use `task-branch` for exploration. This isolates your reasoning from the `main` branch.

### Write-Back Requirements (Resumability)
You must leave the repository in a state where another agent (or yourself in a new session) can resume immediately using `task-context`.

1. **Commit on Success**: If you achieve a milestone (logical fix, feature, test green), run `task-commit`.
2. **Update Summary on Exit**: If you stop without a milestone, you MUST update the active branch's `summary.md`. Update `Current State` and `Next Action`.
3. **Record Evidence**: Log test outputs into your commit or the global `verification.md`.

> [!NOTE]
> GCC commits are focused on **Decisions** and **Rationals**. We care *why* you did something as much as *what* you changed.
