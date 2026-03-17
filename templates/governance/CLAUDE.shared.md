# Claude Shared Governance

## multi-IDE Coordination
You are working in a shared environment with other AI agents (Antigravity, Codex).
To ensure consistency, follow these guidelines:

1. **Read-First Policy**: Always check `docs/project/` for coding standards and architecture before suggesting changes.
2. **Task Directory**: Your task context is located in `docs/task/<ticket-id>/`. Determine the ticket ID from the current Git branch.
3. **Drafting vs. Committing**: If you create a plan, ensure it is saved in `docs/task/<ticket-id>/plan.md`.
4. **No Hidden State**: Do not assume the next session will have access to this chat history. Write everything important to the repo.

## Verification
- Use `docs/project/verify-runbook.md` as the standard for verifying your work.
- Output your verification results to `docs/task/<ticket-id>/verification.md`.
