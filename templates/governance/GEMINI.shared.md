# Geminicli Shared Governance (v1.1)

You are `geminicli`, operating as a command-line AI agent in a multi-agent repository.
Other agents (Codex, Antigravity, Claude) may also be working on this project.
The Git repository is the **only** shared memory between you.

---

## 🚀 SESSION START — Do This First

Do not assume you have any prior context from a previous session. Always start fresh from the repository.

1. **Read `docs/project/context.md`** — ground yourself in what this project is and does.
2. **Read `docs/task/active/task.md`** — understand the current task objective.
3. **Read `docs/task/active/progress.md`** — know what has already been done.
4. **Read `docs/task/active/handoff.md`** — see what the previous agent left for you.
5. Greet the user with a brief status: *"I've loaded the repo context. Active task: [task name]. Previous progress: [1-2 line summary]. Ready to continue."*

---

## 🛑 SESSION END — Do This Before Closing

1. **Append to `docs/task/active/progress.md`** — write what you completed this session. Be specific.
2. **Rewrite `docs/task/active/handoff.md`** — summarize current state and what to do next.
3. If you wrote or changed any code, note the specific files and key changes in the handoff.

---

## 🔧 Common Use Cases for geminicli

This agent is particularly well-suited for:
- **Accepting tasks** from Codex (reading what Codex wrote to `progress.md` and continuing)
- **Code review** — review changes and write findings to `docs/task/active/verification.md`
- **Debug assistance** — trace through errors, propose fixes, update handoff with findings
- **Q&A about the codebase** — answer questions grounded in `docs/project/`

---

## ❌ What You Must NOT Do

- Do not rely on this conversation's history as your project memory
- Do not write canonical state anywhere except `docs/task/active/` and `docs/project/`
- Do not answer questions about the codebase from memory — read the relevant files first
