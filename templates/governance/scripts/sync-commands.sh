#!/bin/bash

# sync-commands.sh
# Syncs neutral command templates from .ai-governance/commands/ to host-specific directories.

GOV_CMD_DIR=".ai-governance/commands"
CLAUDE_CMD_DIR=".claude/commands"
OPENCODE_CMD_DIR=".opencode/commands"
CODEX_PRMPT_DIR=".codex/prompts"
GEMINI_CMD_DIR=".gemini/commands"
AGENT_WF_DIR=".agents/workflows"

# Function to sync
sync_cmd() {
    local cmd_name=$1
    if [ -f "$GOV_CMD_DIR/$cmd_name.md" ]; then
        echo "Syncing $cmd_name..."
        [ -d "$CLAUDE_CMD_DIR" ] && cp "$GOV_CMD_DIR/$cmd_name.md" "$CLAUDE_CMD_DIR/$cmd_name.md"
        [ -d "$OPENCODE_CMD_DIR" ] && cp "$GOV_CMD_DIR/$cmd_name.md" "$OPENCODE_CMD_DIR/$cmd_name.md"
        [ -d "$CODEX_PRMPT_DIR" ] && cp "$GOV_CMD_DIR/$cmd_name.md" "$CODEX_PRMPT_DIR/$cmd_name.md"
        [ -d "$GEMINI_CMD_DIR" ] && cp "$GOV_CMD_DIR/$cmd_name.md" "$GEMINI_CMD_DIR/$cmd_name.md"
        [ -d "$AGENT_WF_DIR" ] && cp "$GOV_CMD_DIR/$cmd_name.md" "$AGENT_WF_DIR/$cmd_name.md"
    fi
}

# Cleanup existing commands before sync to maintain 2-command UI
echo "Cleaning up old commands..."
[ -d "$CLAUDE_CMD_DIR" ] && find "$CLAUDE_CMD_DIR" -type f ! -name "gov-context.md" ! -name "gov-writeback.md" -delete
[ -d "$OPENCODE_CMD_DIR" ] && find "$OPENCODE_CMD_DIR" -type f ! -name "gov-context.md" ! -name "gov-writeback.md" -delete
[ -d "$CODEX_PRMPT_DIR" ] && find "$CODEX_PRMPT_DIR" -type f ! -name "gov-context.md" ! -name "gov-writeback.md" -delete
[ -d "$GEMINI_CMD_DIR" ] && find "$GEMINI_CMD_DIR" -type f ! -name "gov-context.toml" ! -name "gov-writeback.toml" -delete
[ -d "$AGENT_WF_DIR" ] && find "$AGENT_WF_DIR" -type f ! -name "gov-context.md" ! -name "gov-writeback.md" -delete

mkdir -p "$CLAUDE_CMD_DIR" "$OPENCODE_CMD_DIR" "$CODEX_PRMPT_DIR" "$GEMINI_CMD_DIR" "$AGENT_WF_DIR"

sync_cmd "gov-context"
sync_cmd "gov-writeback"

echo "Sync complete."
