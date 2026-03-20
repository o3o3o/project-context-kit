# Project Context Kit v3.2

Project Context Kit adds a durable, repo-local context layer for multi-session and multi-agent work. It stores project memory and active task state in files, so the next agent can resume quickly without depending on chat history or IDE memory.

Its main pain point is practical context recovery across tools and sessions: in Codex, Antigravity, OpenCode, Gemini, and similar IDE or TUI editors, `/ctx-load` and `/ctx-save` make it easier to preserve project progress, switch tools, and quickly restore working context in a new session.

Project Context Kit 为仓库增加一层可持久化、可版本化的上下文。它把项目级知识和当前任务状态写入文件，让下一个 agent 或下一次会话可以快速接手，而不依赖聊天记录或 IDE 内存。

它要解决的核心痛点很实际：在 Codex、Antigravity、OpenCode、Gemini 等 IDE / TUI 编辑器之间切换时，或者在不同 session 之间继续工作时，可以通过 `/ctx-load` 和 `/ctx-save` 保存项目进度，并快速把上下文拿回来。

> [!IMPORTANT]
> Project Context v3.2 uses `.project-context/` as the primary storage path and `/ctx-load` plus `/ctx-save` as the default command pair.

> [!NOTE]
> This kit was influenced by the Git Context Control paper. Internally, a few files may still mention the older GCC architecture name, but the user-facing model is now Project Context.

## English

### What It Is

This kit separates durable context into two layers:

- **Project memory**: stable repo knowledge such as commands, architecture, standards, and long-lived lessons.
- **Task memory**: the current active task, current status, verification notes, and the next step.

The default model is a **single active task**. Advanced parallel workstreams are available when needed, but they are not the default path.

### When To Use It

Project Context is most useful when:

- You switch between repositories often and need fast context recovery.
- Multiple agents take turns on the same codebase.
- A task spans multiple sessions or several days.
- You want task state to survive chat resets, editor restarts, or agent changes.
- You want a simple resumable handoff without forcing everyone to read a long conversation.

It is intentionally less about "governance paperwork" and more about "fast, reliable project resume".

### Core Workflow

Use these two commands:

- `/ctx-load`: load the current project context at the start of a session.
- `/ctx-save`: write back the current task state before ending a session.

Default storage layout:

- `.project-context/docs/project/metadata.yaml`
- `.project-context/docs/project/context.md`
- `.project-context/docs/task/active/index.md`
- `.project-context/docs/task/active/task.md`
- `.project-context/docs/task/active/summary.md`
- `.project-context/docs/task/active/verification.md`

### Simple Mode vs Advanced Mode

- **Simple mode**: everything lives under `docs/task/active/`. This is the default and recommended mode.
- **Advanced mode**: use `docs/task/active/workstreams/<name>/` only for parallel experiments, risky explorations, or true multi-agent branching work.

### Installation

```bash
# Install or update Project Context
python3 installer/install.py

# Install and migrate an older .ai-governance repo
python3 installer/install.py --migrate

# Install, migrate, and auto-clean legacy files
python3 installer/install.py --migrate --yes

# Shell wrapper
./installer/install.sh . --migrate --yes
```

### Migration From `.ai-governance`

If your repo still uses `.ai-governance/`, you have two options:

```bash
# Integrated migration during install
python3 installer/install.py --migrate

# Standalone migration script
python3 scripts/migrate_to_project_context.py --target /path/to/repo
```

Migration behavior:

- Copies legacy data into `.project-context/` without overwriting newer files.
- Migrates `docs/project/*.md`.
- Migrates `docs/task/active/*.md`.
- Migrates legacy `branches/main/summary.md` into the new active-task files when needed.
- Rewrites root instructions from old paths and old command names to the new ones.
- Can optionally delete legacy `.ai-governance/` and old `gov-*` command files after confirmation.

### Hermetic Rule

All shared context should be self-contained inside `.project-context/`.

- Do not link to temporary files in `/tmp`.
- Inline small logs into task docs when possible.
- Move larger artifacts into `docs/task/active/assets/`.

## 中文说明

### 这是什么

这套工具的目标不是做“很重的治理系统”，而是做一套**适合长期协作的项目上下文层**。

它把上下文拆成两层：

- **项目层记忆**：比如命令、架构、代码规范、长期有效的经验。
- **任务层记忆**：比如当前目标、当前进度、验证结果、下一步动作。

默认模型是**单活动任务模型**，也就是日常只维护一个 `active task`。如果确实需要并行探索，再进入 `workstreams`。

### 适合什么场景

这套工具特别适合这些场景：

- 你经常切换项目，希望 1 分钟内恢复上下文。
- 同一个仓库会被多个 agent 接力处理。
- 一个任务跨多次会话、多天推进。
- 你不想把真实状态只放在聊天记录里。
- 你希望“下一个人/下一个 agent”能直接从文件接手。

一句话说，它的重点是：
**快速恢复上下文，降低切项目和换 agent 的成本。**

### 日常怎么用

默认只需要记住两个命令：

- `/ctx-load`：开始会话时加载上下文
- `/ctx-save`：结束会话前写回任务状态

默认目录结构：

- `.project-context/docs/project/metadata.yaml`
- `.project-context/docs/project/context.md`
- `.project-context/docs/task/active/index.md`
- `.project-context/docs/task/active/task.md`
- `.project-context/docs/task/active/summary.md`
- `.project-context/docs/task/active/verification.md`

### 简单版和高级版

- **简单版**：默认模式。所有状态都放在 `docs/task/active/` 下。
- **高级版**：只有在并行实验、风险探索、多人并行分线时，才使用 `docs/task/active/workstreams/<name>/`。

建议大多数仓库都先用简单版。

### 安装与迁移

```bash
# 安装或更新
python3 installer/install.py

# 安装时顺便迁移旧 .ai-governance 仓库
python3 installer/install.py --migrate

# 安装、迁移，并自动清理旧文件
python3 installer/install.py --migrate --yes

# shell 包装脚本
./installer/install.sh . --migrate --yes
```

如果你是旧仓库，也可以单独运行迁移脚本：

```bash
python3 scripts/migrate_to_project_context.py --target /path/to/repo
python3 scripts/migrate_to_project_context.py --target /path/to/repo --yes
```

迁移时会做这些事：

- 把旧 `.ai-governance/` 内容同步到新的 `.project-context/`
- 复制 `docs/project/*.md`
- 复制 `docs/task/active/*.md`
- 必要时把旧 `branches/main/summary.md` 升级成新的 `active/summary.md` 和 `active/index.md`
- 把根目录说明文件里的旧路径和旧命令改成新名字
- 在确认迁移成功后，可选择删除旧 `.ai-governance/` 和旧 `gov-*` 命令文件

### 使用建议

- 切项目频繁时，优先看 `index.md`
- 普通会话默认只更新 `summary.md`
- 到 milestone 再写 `commits/`
- 不要把 `workstreams` 当默认入口
- 重要验证信息放进 `verification.md` 或 `assets/`

## Repository Data

- **Logic**: stored in `.agents/` at the project root
- **Data**: stored in `.project-context/`
