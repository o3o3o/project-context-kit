# GCC (Git-Context-Controller) Model v3.0

This kit installs a **Git-Context-Controller (GCC)** memory layer. It treats AI agent context as a versioned engineering artifact, allowing multiple agents to collaborate seamlessly across sessions.

> [!IMPORTANT]
> **GCC v3.0 (Hermetic Model)**: This version introduces **Tiered Memory** and **Hermetic Commitments**, ensuring that project knowledge is preserved while task progress remains durable and self-contained.

---

## ⚡ Two-Command Workflow

The entire GCC lifecycle is managed through two entry points. These are the ONLY commands you need to remember.

### 1. `/gov-context` (Punch-In)
**When**: Immediately upon starting a new session.
**Behavior**: 
- **Tier 1 (Project)**: Reads architecture, standards, and history from `docs/project/`.
- **Tier 2 (Task)**: Synthesizes the current active branch objective and latest progress.
- **Auto-Boot**: Automatically offers to initialize the repository if GCC is not found.

### 2. `/gov-writeback` (Punch-Out)
**When**: Just before ending your session.
**Behavior**: 
- **Knowledge Extraction**: Prompts the agent to move universal "lessons learned" to the Project Tier.
- **Hermetic Check**: Ensures all external evidence (logs/artifacts) are inlined or moved to `.ai-governance/assets/`.
- **State Capture**: Automatically decides whether to create a structured `commit` or just update the `summary.md`.

---

## 🏗 The Tiered Hierarchy

### Tier 1: Project Memory (Permanent)
Located in `.ai-governance/docs/project/`.
- **`metadata.yaml`**: The "User Manual" for the repo (build/test/install commands).
- **`context.md`**: The "Project Brain." Contains architecture, domain knowledge, and cumulative lessons learned.

### Tier 2: Task Memory (Ephemeral)
Located in `.ai-governance/docs/task/active/`.
- **`task.md`**: The current mission objective.
- **`summary.md`**: The "resumable image" of the current branch state.
- **`assets/`**: Permanent storage for logs, screenshots, and evidence referenced in governance files.
- **`commits/`**: A chain of structured decisions ("The Why") behind the code changes.

---

## 🛡 The Hermeticity Rule
To ensure that any agent can resume work on any machine, **all governance records must be self-contained.**

1. **No External Links**: Never reference a file in `/tmp` or `artifacts/` in your reports.
2. **Evidence Inlining**: Small logs and text evidence must be inlined directly into `verification.md` or a commit.
3. **Evidence Capture**: Large artifacts must be moved to `docs/task/active/assets/` before being linked.

---

## 🔧 Installation & Setup

```bash
# Install/Update GCC in your repository
python3 installer/install.py
```

- **Logic**: Stored in `.agents/` (plural) at the project root.
- **Data**: Stored in `.ai-governance/` (hidden) to prevent cluttering the main source tree.
