# /ctx-save
Write back the current working state for the next agent.

Update:
- `.project-context/docs/task/active/index.md`
- `.project-context/docs/task/active/summary.md`
- `.project-context/docs/task/active/verification.md` when validation changed

If `verification.md` explicitly says `Status: Complete` or `Status: Done`, archive the completed task snapshot before ending the session.

Move:
- `index.md`
- `task.md`
- `summary.md`
- `verification.md`
- `commits/` if present
- `assets/` if present
- `workstreams/` if present

From:
- `.project-context/docs/task/active/`

Into:
- `.project-context/docs/task/archive/YYYY-MM-DD-<slug>/`

Then recreate `.project-context/docs/task/active/` from `.project-context/docs/task/_template/`.

Rules:
- Overwrite instead of append
- Keep it concise and recovery-oriented
- Only include information useful for resuming work
- Be explicit about uncertainty or incomplete validation
- Do not leave completed task content in `active/`
