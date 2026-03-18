# Geminicli Shared Governance (v2.1 - GCC Memory Model)

You are `geminicli`. We use a **Git-Context-Controller (GCC)** memory model for durable collaboration.

> [!IMPORTANT]
> GCC objects (commits/branches) are governance-level files in `.ai-governance/docs/`. They are not native Git commits.

---

## 🚀 SESSION START

1. **Load Metadata**: Read `.ai-governance/docs/project/metadata.yaml` to know which commands (`run`, `test`) to use.
2. **Load View**: Run `task-context` to see the current active branch and latest commit.
3. Greet: *"GCC context loaded. Branch: [branch]. Ready to proceed."*

---

## 🛑 SESSION END

1. **Checkpointing**:
   - If work was completed: Run `task-commit`.
   - If only partial progress: Update `summary.md` (Current State / Next Action).
2. **Verification**: Record any CLI output evidence in your commit or `docs/task/active/verification.md`.

---

## 🔧 GCC Branching
If the user asks for a risky experiment, run `task-branch <name>` first. This creates a safe directory for your exploration commits.

---

## ❌ Constraints
- Do not append to a single log file. Use the GCC tree.
- Do not ignore `metadata.yaml`. It is the source of truth for repository structure.
