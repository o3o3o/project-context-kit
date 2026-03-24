# project-context-kit

project-context-kit is a small repo-local context system for coding agents.

It solves one specific problem: when you switch between Codex, Antigravity, OpenCode, Gemini, or different sessions, the working context is usually trapped in chat history or editor memory. This kit stores the important project and task state in files, so another agent can resume quickly with `/ctx-load` and leave an accurate handoff with `/ctx-save`.

## What You Install

This kit installs:

- `.project-context/` for durable project and task context
- `.agents/` for shared skill and workflow definitions
- root instruction blocks in `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md`

After installation, the target repository gets a standard structure like:

- `.project-context/docs/project/metadata.yaml`
- `.project-context/docs/project/context.md`
- `.project-context/docs/task/active/index.md`
- `.project-context/docs/task/active/task.md`
- `.project-context/docs/task/active/summary.md`
- `.project-context/docs/task/active/verification.md`

The installer seeds these active task files so the first `/ctx-load` has something to read immediately.

## When To Use It

Use this when:

- you switch between multiple agent IDEs or TUI editors
- one repo is handled by multiple agents over time
- a task spans multiple sessions or multiple days
- you want durable handoff state in files instead of chat logs
- you want fast project resume with minimal startup cost

Do not think of it as a heavy governance system. It is a practical project resume layer.

## Install

From this repository, install into a target project directory:

```bash
./installer/install.sh /path/to/your-project
```

Equivalent Python form:

```bash
python3 installer/install.py --target /path/to/your-project
```

Example:

```bash
./installer/install.sh ~/work/my-app
```

That command modifies the target repository, not this kit repository.

## Daily Workflow

At the start of a session:

- run `/ctx-load`
- read the active task state
- rewrite placeholder starter content if this is the first real session
- continue work

Before ending a session:

- run `/ctx-save`
- update `index.md`, `summary.md`, and `verification.md` as needed
- leave the next step for the next agent or next session

## Model

This kit uses a single active task by default.

- **Project memory**: durable repo knowledge such as commands, architecture, standards, and long-lived lessons
- **Task memory**: the current active goal, current progress, verification state, and next action

Simple mode is the default:

- everything lives under `.project-context/docs/task/active/`

Advanced mode is optional:

- use `.project-context/docs/task/active/workstreams/<name>/` only when you really need parallel exploration

## Why It Helps

Without this kit:

- context is lost when you switch editors or sessions
- handoff quality depends on memory and chat history
- each new agent spends time rediscovering current state

With this kit:

- project state is stored in files inside the repo
- context becomes portable across tools and sessions
- startup cost for the next agent is much lower

## Notes

- `.project-context/` is the durable data layer
- `.agents/` is the logic layer
- large evidence should go into `.project-context/docs/task/active/assets/`
- important validation should be recorded in `verification.md`

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE).
