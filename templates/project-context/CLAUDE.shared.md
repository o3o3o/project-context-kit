# Claude Shared Project Context (v3.2)

You are operating in a multi-agent repository using a **Project Context** memory model.

> [!NOTE]
> Project Context records focus on resumable context: what matters now, why it changed, and what should happen next.

---

## 🚀 CONTEXT SYNC

Use `context-load` when you need to reconstruct durable task state or validate a handoff. It does not need to be the first action of every session.

1. **Read Metadata**: Load `.project-context/docs/project/metadata.yaml`. It contains the commands you need to build and test.
2. **Read Project Context**: Load `.project-context/docs/project/context.md` for architecture, standards, and durable project knowledge.
3. **Read Active Index**: Load `.project-context/docs/task/active/index.md` for the fastest current-state view.
4. **Execute `context-load` When Needed**: Run this skill when the session needs task reconstruction from durable context.
5. **Bootstrap If Needed**: If the active task files do not exist yet, initialize them from `.project-context/docs/task/_template/` or run `context-bootstrap`.
6. **Sync with User**: Tell the user: *"I've read the project context. Status: [status]. Proceeding with [Action]."* when you actually performed the load.

---

## 🛑 SESSION END — Do This Before Stopping

You must leave the repository in a state where another agent can pick up your work without reading the chat history.

1. **Always Refresh Active State**: Update `.project-context/docs/task/active/index.md` and `.project-context/docs/task/active/summary.md`.
2. **Milestone Reached?**: If you completed a feature, fix, or hypothesis test, run `context-checkpoint`.
3. **Evidence**: Write any validation results into the commit or `.project-context/docs/task/active/verification.md`.

---

## ❌ Rules

- **No `progress.md`**: It is deprecated.
- **No `handoff.md`**: Use `summary.md`.
- **Metadata First**: Always check `metadata.yaml` before guessing directory structures or build commands.
- **Durable State**: Only files in `.project-context/docs/` are shared context. Your internal thoughts/artifacts are private to this session.
