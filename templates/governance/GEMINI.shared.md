# Geminicli Shared Governance (v2.1 - GCC Memory Model)

You are `geminicli`. We use a **Git-Context-Controller (GCC)** memory model for durable collaboration.

> [!IMPORTANT]
> GCC objects (commits/branches) are governance-level files in `.ai-governance/docs/`. They are not native Git commits.

---

## 🛠 SKILLS & TOOLS

You have access to specialized governance skills in `.agents/skills/`. You MUST use the `activate_skill` tool to load them.

- `task-context`: **Always run this first.** It reconstructs the project and task state from the GCC tree.
- `task-commit`: Run this to create a milestone commit when you reach a valid change.
- `task-bootstrap`: Run this to initialize a new GCC task tree.
- `task-branch`: Create a new reasoning branch for risky experiments.
- `task-merge`: Merge an exploration branch back to main.

---

## 🚀 SESSION START

1. **Load Metadata**: Read `.ai-governance/docs/project/metadata.yaml` to know which commands (`run`, `test`) to use.
2. **Load View**: Call `activate_skill(name="task-context")` to see the current active branch and latest commit.
3. Greet: *"GCC context loaded. Branch: [branch]. Ready to proceed."*

---

## 🛑 SESSION END

1. **Checkpointing**:
   - If work was completed: Call `activate_skill(name="task-commit")`.
   - If only partial progress: Update `summary.md` (Current State / Next Action) directly.
2. **Verification**: Record any CLI output evidence in your commit or `docs/task/active/verification.md`.

---

## ❌ Constraints
- Do not append to a single log file. Use the GCC tree.
- Do not ignore `metadata.yaml`. It is the source of truth for repository structure.
