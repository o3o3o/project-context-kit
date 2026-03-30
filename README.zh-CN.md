# project-context-kit

project-context-kit 是一套给 coding agent 使用的、仓库内本地化的上下文系统。

它解决的是一个很具体的问题：当你在 Codex、Antigravity、OpenCode、Gemini 或不同 session 之间切换时，工作上下文通常只存在于聊天记录或编辑器状态里。这套工具把关键的项目状态和任务状态写入文件，让下一个 agent 可以通过 `/ctx-load` 快速接手，并通过 `/ctx-save` 留下可恢复的进度。

## 会安装什么

这套工具会安装：

- `.project-context/` 用来保存项目级和任务级上下文
- `.agents/` 用来保存共享的 skill 和 workflow 定义
- 在 `AGENTS.md`、`CLAUDE.md`、`GEMINI.md` 中写入统一入口说明

安装后，目标仓库会得到类似这样的结构：

- `.project-context/docs/project/metadata.yaml`
- `.project-context/docs/project/context.md`
- `.project-context/docs/decisions/`
- `.project-context/docs/task/active/index.md`
- `.project-context/docs/task/active/task.md`
- `.project-context/docs/task/active/summary.md`
- `.project-context/docs/task/active/verification.md`

安装器现在会直接 seed 这些 active task 文件，这样第一次 `/ctx-load` 就有可读内容，而不是只有空目录。

## 适合什么场景

适合这些场景：

- 你经常在多个 agent IDE 或 TUI 编辑器之间切换
- 同一个仓库会被多个 agent 分时接力处理
- 一个任务跨多次 session 或多天推进
- 你希望把 handoff 状态写进文件，而不是只留在聊天记录里
- 你希望下一个 agent 的启动成本尽量低

不要把它理解成很重的治理系统。它本质上是一个实用的项目恢复层。

## 安装

在当前仓库里执行，把它安装到你的目标项目目录：

```bash
./installer/install.sh /path/to/your-project
```

等价的 Python 形式：

```bash
python3 installer/install.py --target /path/to/your-project
```

示例：

```bash
./installer/install.sh ~/work/my-app
```

这个命令修改的是目标项目仓库，不是当前这个 kit 仓库。

## 日常工作流

开始一个 session 时：

- 运行 `/ctx-load`
- 读取当前 active task 状态
- 如果还是初始占位内容，先改成真实任务信息
- 继续执行开发工作

结束一个 session 前：

- 运行 `/ctx-save`
- 按需要更新 `index.md`、`summary.md`、`verification.md`
- 为下一个 agent 或下一次 session 留下明确的下一步

## 模型

这套工具默认使用单活动任务模型。

- **项目层记忆**：比如命令、架构、规范、长期有效的经验
- **项目级决策**：比如应该长期沿用的轻量设计结论
- **任务层记忆**：比如当前目标、当前进度、验证状态、下一步动作

默认是简单模式：

- 所有主要状态都在 `.project-context/docs/task/active/`

高级模式是可选的：

- 只有在确实需要并行探索时，才使用 `.project-context/docs/task/active/workstreams/<name>/`

## 它解决了什么问题

没有这套工具时：

- 一切上下文都容易在切 IDE 或切 session 时丢失
- handoff 质量依赖记忆和聊天记录
- 新 agent 需要花时间重新判断当前状态

有了这套工具后：

- 项目状态被保存到仓库文件中
- 上下文可以跨工具、跨 session 搬运
- 下一个 agent 的启动成本会低很多

## 说明

- `.project-context/` 是持久化数据层
- `.agents/` 是逻辑层
- `docs/decisions/` 用来放轻量、长期有效的设计决策
- 大体积证据放到 `.project-context/docs/task/active/assets/`
- 重要验证结果写入 `verification.md`

## License

本项目使用 MIT License。详见 [LICENSE](./LICENSE)。
