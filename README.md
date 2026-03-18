# Repo Governance Kit

A plug-in governance layer that enables **Antigravity, Codex, Claude, and geminicli** to collaborate on the same project without losing context between sessions or agent switches.

## The Problem
When you switch AI tools mid-task — say from Codex to Claude, or to `geminicli` — all the context from your previous session is gone. Each agent starts fresh from its own chat history. This creates:
- Repetitive re-explanations of the codebase
- Conflicting decisions made by different agents
- Lost work from forgotten handoffs

## The Solution: Repository as Shared Memory
This kit installs a lightweight governance layer that makes your **Git repository** the sole durable memory. Every agent reads from and writes to the same directory structure.

## Core Concept: Active Task
There is always one active task in `.ai-governance/docs/task/active/`. No branch mapping, no ticket IDs in paths. Every agent reads from the same place:
```
.ai-governance/docs/task/active/
  task.md          ← What we're trying to do
  plan.md          ← How we plan to do it
  progress.md      ← Running log of what's been done
  handoff.md       ← State and next steps for the incoming agent
  verification.md  ← Test evidence
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
1. Append to `.ai-governance/docs/task/active/progress.md` — what it completed
2. Rewrite `.ai-governance/docs/task/active/handoff.md` — where things stand and what to do next

**Incoming agent (geminicli) must:**
1. Run `task-resume` skill (or manually read `progress.md` and `handoff.md`)
2. Announce to you what state it sees before doing anything

## Workflow: Closing a Task

Tell your agent: *"Run task-archive"*. It will:
1. Move `.ai-governance/docs/task/active/` to `.ai-governance/docs/task/archive/<date-name>/`
2. Write a final status to the archived `handoff.md`
3. Clear `.ai-governance/docs/task/active/` for the next task

---

## Available Skills

| Skill | What it does |
|-------|-------------|
| `task-bootstrap` | Initialize `.ai-governance/docs/task/active/` for a new task |
| `task-resume` | Read and summarize the current active task |
| `task-archive` | Archive the completed task and clear active/ |
| `verify-change` | Run verification and write results to verification.md |

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
│       │   ├── context.md
│       │   ├── architecture.md
│       │   ├── coding-standards.md
│       │   └── verify-runbook.md
│       └── task/
│           ├── active/    ← Current task (always here, no branch mapping)
│           ├── archive/   ← Completed tasks
│           └── _template/ ← Templates for new tasks
```

---

## The "Write-Back" Contract

Every agent **must** update these two files before ending a session:

1. **`.ai-governance/docs/task/active/progress.md`** — Append what you did (be specific: file names, what changed)
2. **`.ai-governance/docs/task/active/handoff.md`** — Rewrite to reflect current state and what to do next

This is how the next agent (or tomorrow's you) picks up exactly where things left off.
# repo-governance-kit
