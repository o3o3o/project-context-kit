Before ending the session, write back the resumable task state.

Update:
- `.project-context/docs/task/active/index.md`
- `.project-context/docs/task/active/summary.md`
- `.project-context/docs/task/active/verification.md` when validation changed

If `verification.md` explicitly says `Status: Complete` or `Status: Done`, you must archive the completed task snapshot before ending the session.

Move:
- `.project-context/docs/task/active/index.md`
- `.project-context/docs/task/active/task.md`
- `.project-context/docs/task/active/summary.md`
- `.project-context/docs/task/active/verification.md`
- `.project-context/docs/task/active/commits/` if present
- `.project-context/docs/task/active/assets/` if present
- `.project-context/docs/task/active/workstreams/` if present

Into:
- `.project-context/docs/task/archive/YYYY-MM-DD-<slug>/`

Then recreate `.project-context/docs/task/active/` from `.project-context/docs/task/_template/`.

Rules:
- overwrite instead of append
- concise and practical
- optimize for fast resume by another agent
- clearly mark uncertainty
- do not leave completed task content in `active/`
