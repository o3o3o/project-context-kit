# /ctx-save
Write the current resumable task state to:
- `.project-context/docs/task/active/index.md`
- `.project-context/docs/task/active/summary.md`
- `.project-context/docs/task/active/verification.md` when validation changed

If `verification.md` explicitly says `Status: Complete` or `Status: Done`, archive the completed task snapshot before ending the session.

Move the current `.project-context/docs/task/active/` task snapshot into:
- `.project-context/docs/task/archive/YYYY-MM-DD-<slug>/`

Then recreate `.project-context/docs/task/active/` from `.project-context/docs/task/_template/`.

Constraints:
- overwrite, do not append
- concise only
- focus on resumability
- clearly mark incomplete or unverified items
- do not leave completed task content in `active/`
