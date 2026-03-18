# Geminicli Shared Governance (v2.0 - GCC Memory Model)

You are `geminicli`, operating as a command-line AI agent in a multi-agent repository.
We use a **Git-Context-Controller (GCC)** memory model. 

---

## 🚀 SESSION START — Do This First

1. **Read Metadata**: `.ai-governance/docs/project/metadata.yaml` provides your execution constraints.
2. **Load Context View**: Read `.ai-governance/docs/task/active/task.md` and the active branch's `summary.md`. If there are commits, read the most recent one in `.ai-governance/docs/task/active/branches/<branch>/commits/`.
3. Greet the user: *"I've loaded the GCC state. Active branch: [branch]. Latest commit: [summary]. Ready to continue."*

---

## 🛑 SESSION END — Do This Before Closing

1. **Execute Commit**: You must write a new commit file to the active branch's `commits/` directory documenting what you accomplished.
2. **Update Branch Summary**: Update `summary.md` with the new status and next steps.

---

## 🔧 GCC Branching for Geminicli

If you are asked to debug or explore a radical change:
- Create a new directory under `.ai-governance/docs/task/active/branches/` for your exploration.
- This isolates your reasoning commits from the main path.
- When done, summarize your findings in that branch's `summary.md`.

---

## ❌ What You Must NOT Do

- Do not ask for `progress.md` — it has been replaced by structured `commits/`.
- Do not write canonical state anywhere except the GCC tree in `.ai-governance/docs/task/active/`.
