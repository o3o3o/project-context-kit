# Repo Governance Kit

A plug-in governance layer that enables **Antigravity, Codex, Claude, and geminicli** to collaborate on the same project without losing context between sessions or agent switches.

## The Problem
When you switch AI tools mid-task — say from Codex to Claude, or to `geminicli` — all the context from your previous session is gone. Each agent starts fresh from its own chat history. This creates:
- Repetitive re-explanations of the codebase
- Conflicting decisions made by different agents
- Lost work from forgotten handoffs

## The Solution: Git-Context-Controller (GCC) Model
This kit installs a **Git-Context-Controller (GCC)** memory layer that makes your Git repository the sole durable memory for all agents. 

We don't use simple linear prompt histories or a long appended `progress.md`. We use a structured, tree-like approach mirroring Git itself:
- **Commits**: Discrete milestones of work (Intent, Changes, Decisions).
- **Branches**: Isolated paths for experimental exploration.

## Core Concept: The Active GCC Tree
There is always one active task in `.ai-governance/docs/task/active/`. Before touching code, agents read the root `metadata.yaml` to understand execution constraints. 
```
.ai-governance/docs/
  ├── project/            ← Global context (metadata, architecture)
  └── task/active/
      ├── task.md         ← Main objective
      └── branches/
          └── main/
              ├── summary.md        ← Current branch status (replaces handoff)
              └── commits/          ← Discrete structured commits of work
                  ├── 2026-03-A.md
                  └── 2026-03-B.md
```
When a task closes, run `task-archive` to move it to `.ai-governance/docs/task/archive/<date-name>/`.

---

## Installation

```bash
# Install into current directory
path/to/repo-governance-kit/installer/install.sh .

# Or with Python directly
python3 path/to/repo-governance-kit/installer/install.py --target .
```

This will:
- Install `.ai-governance/` with shared rules, skills, and documentation
- Copy `.ai-governance/docs/project/` templates (non-destructive)
- Create `.ai-governance/docs/task/active/` and `.ai-governance/docs/task/archive/`
- Merge governance blocks into `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md`

## Upgrading
Just re-run the installer. It will update the `.ai-governance/` layer including documentation structure.

---

## Recommended Agent Roles

| Agent | Best For |
|-------|---------|
| **Codex** | Main implementation — write code, run tests |
| **geminicli** | Pick up where Codex left off, debug, code review |
| **Claude** | Code review, hardening, complex debugging |
| **Antigravity** | Architecture planning, repo research, final diff review |

---

## Workflow: Starting a New Task

1. Tell your agent (any of them): *"Run task-bootstrap"*
2. The agent creates `.ai-governance/docs/task/active/` with all 5 template files
3. Fill in `task.md` with the objective
4. Start working — the agent will read from and write to this directory

## Workflow: Switching Agents

When switching from Codex to geminicli (or any combination):

**Outgoing agent (Codex) must:**
1. Run `task-commit` to document its completed work in the active branch.
2. The skill automatically updates the `summary.md`.

**Incoming agent (geminicli) must:**
1. Run `task-context` skill to build a dynamic view of the current GCC state.
2. Announce to you what context it sees before doing anything.

## Workflow: Exploring Branches

If you're unsure of an approach and want to prototype:
1. Run `task-branch` and name it (e.g., `explore-db`).
2. Make your commits there.
3. If it works, run `task-merge` to merge the findings back into `main`.

## Workflow: Closing a Task

Tell your agent: *"Run task-archive"*. It will:
1. Move the entire GCC tree to `.ai-governance/docs/task/archive/<date-name>/`
2. Write a final status to the archived `summary.md`
3. Clear `.ai-governance/docs/task/active/` for the next task

---

## Available Skills

| Skill | What it does |
|-------|-------------|
| `task-bootstrap` | Initialize `.ai-governance/docs/task/active/` for a new task |
| `task-context` | Synthesize current GCC state (Replaces `task-resume`) |
| `task-archive` | Archive the completed task and clear active/ |
| `task-commit` | Create a structured context commit |
| `task-branch` | Fork into an isolated exploration branch |
| `task-merge` | Merge an exploration branch back to main |
| `verify-change` | Run verification and write results |

---

## Post-Installation Structure

```
your-repo/
├── AGENTS.md              ← Antigravity/Codex entry (governance block appended)
├── CLAUDE.md              ← Claude entry (governance block appended)
├── GEMINI.md              ← geminicli entry (governance block appended)
├── .ai-governance/
│   ├── AGENTS.shared.md   ← Startup/shutdown protocol for all agents
│   ├── CLAUDE.shared.md   ← Claude-specific instructions
│   ├── GEMINI.shared.md   ← geminicli-specific instructions
│   ├── repo-contract.md   ← Cross-agent rules
│   ├── .agents/
│   │   ├── rules/
│   │   │   └── 00-repo-contract.md
│   │   └── skills/
│   │       ├── task-bootstrap/
│   │       ├── task-resume/
│   │       ├── task-archive/
│   │       └── verify-change/
│   └── docs/              ← Consolidated governance documentation
│       ├── project/
│       │   ├── metadata.yaml
│       │   ├── context.md
│       │   ├── architecture.md
│       │   ├── coding-standards.md
│       │   └── verify-runbook.md
│       └── task/
│           ├── active/    ← Local GCC tree
│           │   ├── task.md
│           │   └── branches/
│           │       └── main/
│           │           ├── summary.md
│           │           └── commits/
│           └── archive/   ← Completed tasks
```

---

## The "Write-Back" Contract

Every agent **must** create a commit before ending a session.

1. **Commit**: Summarize your changes, intents, and decisions.
2. **Update Summary**: The CLI skill will update `summary.md` with the next action.

This is how the next agent (or tomorrow's you) parses exactly how we arrived at the current state, without navigating an infinitely long progress log.
# repo-governance-kit
