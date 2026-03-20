# project-context-kit

A repo-local context layer for coding agents across tools and sessions.

一个面向 coding agent 的仓库内上下文层，用于跨工具、跨 session 恢复项目进度。

- [English](./README.en.md)
- [中文](./README.zh-CN.md)

## Quick Install

Install into your target project directory:

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

This command modifies the target repository, not this kit repository.

## What It Solves

When you switch between Codex, Antigravity, OpenCode, Gemini, or different sessions, working context is often trapped in chat history or editor state. project-context-kit stores the important project and task state in repo files, so the next agent can resume with `/ctx-load` and leave state with `/ctx-save`.

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE).
