# Claude Shared Governance (v2.0 - GCC Memory Model)

You are operating in a multi-agent repository using a **Git-Context-Controller (GCC)** memory model.
Instead of a simple progress file, we use `commits/` and `branches/` to structure agent memory.

---

## 🚀 SESSION START — Do This First

Before writing any code or making any suggestions:

1. **Read Context**: Read `.ai-governance/docs/project/metadata.yaml` and `.ai-governance/docs/project/context.md`.
2. **Execute `task-context`**: Run the `task-context` skill (or manually view `.ai-governance/docs/task/active/task.md` + `.ai-governance/docs/task/active/branches/main/summary.md` + the latest file in `commits/`).
3. Tell the user: *"I've read the GCC context. Active branch: [name]. Latest commit was: [summary]. I'll continue from there."*

> **Do not skip this.** Skipping means you are working from your conversation history, not the repository GCC state.

---

## 🛑 SESSION END — Do This Before Stopping

Before finishing or before the user closes the conversation:

1. **Always Commit**: Run the `task-commit` skill (or manually create a markdown file in `.ai-governance/docs/task/active/branches/[active-branch]/commits/` following the `_commit_template.md`).
2. **Content of Commit**: Document the *Intent*, *Changes Made*, *Decisions*, and *Next Steps*. 
3. **Update Summary**: Ensure `.ai-governance/docs/task/active/branches/[active-branch]/summary.md` is updated so the next agent knows what is blocking or what is next.

---

## ❌ What You Must NOT Do

- Do not attempt to append to `progress.md` (it is deprecated).
- Do not rely on chat history. If you explore an alternative idea, create a new branch directory in `branches/`.
- Do not write task state into `CLAUDE.md`.

---

## ✅ Verification

Use `.ai-governance/docs/project/verify-runbook.md` as your checklist.
Write verification results into your commit.
