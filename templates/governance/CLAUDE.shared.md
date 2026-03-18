# Claude Shared Governance (v1.1)

You are operating in a multi-agent repository. Other agents (Codex, Antigravity, geminicli) may also work on this same codebase. The Git repository is the **only** shared state between you.

---

## 🚀 SESSION START — Do This First

Before writing any code or making any suggestions:

1. **Read `.ai-governance/docs/project/context.md`** — understand the project's tech stack and goals.
2. **Read `.ai-governance/docs/task/active/task.md`** — understand what the current task is.
3. **Read `.ai-governance/docs/task/active/progress.md`** — understand what has already been done.
4. **Read `.ai-governance/docs/task/active/handoff.md`** — understand what the previous agent left for you.
5. Tell the user: *"I've read the active task. We are working on [task name]. The last status was: [summary from progress.md]. I'll continue from there."*

> **Do not skip this.** Skipping means you are working from your conversation history, not the repository state — which is wrong.

---

## 🛑 SESSION END — Do This Before Stopping

Before finishing or before the user closes the conversation:

1. **Write to `.ai-governance/docs/task/active/progress.md`** — append what you did this session with specifics (not "reviewed code", but "fixed bug in `auth.py:L45` where token was not refreshed on 401").
2. **Rewrite `.ai-governance/docs/task/active/handoff.md`** — make it clear for whoever picks this up next:
   ```
   ## Status
   [brief state summary]
   ## Accomplished this session
   - ...
   ## Next steps
   - ...
   ## Blockers
   - ...
   ```
3. If you found a bug you didn't fix, note it in handoff under "Blockers".
4. If you made architectural discoveries, update `.ai-governance/docs/project/architecture.md`.

---

## ❌ What You Must NOT Do

- Do not treat chat history as canonical state
- Do not tell the user to "check what we discussed earlier" — they may have switched agents
- Do not skip handoff updates because you think the human will remember
- Do not write task state into `CLAUDE.md` — only write it to `.ai-governance/docs/task/active/`

---

## ✅ Verification

Use `.ai-governance/docs/project/verify-runbook.md` as your verification checklist.
Write all verification results to `.ai-governance/docs/task/active/verification.md`.
