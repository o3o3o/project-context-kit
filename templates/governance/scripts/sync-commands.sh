#!/bin/bash

# sync-commands.sh
# Syncs neutral command templates from .ai-governance/commands/ to host-specific directories.

GOV_CMD_DIR=".ai-governance/commands"
CLAUDE_CMD_DIR=".claude/commands"
OPENCODE_CMD_DIR=".opencode/commands"
CODEX_PRMPT_DIR=".codex/prompts"

# Function to sync
sync_cmd() {
    local cmd_name=$1
    if [ -f "$GOV_CMD_DIR/$cmd_name.md" ]; then
        echo "Syncing $cmd_name..."
        [ -d "$CLAUDE_CMD_DIR" ] && cp "$GOV_CMD_DIR/$cmd_name.md" "$CLAUDE_CMD_DIR/$cmd_name.md"
        [ -d "$OPENCODE_CMD_DIR" ] && cp "$GOV_CMD_DIR/$cmd_name.md" "$OPENCODE_CMD_DIR/$cmd_name.md"
        [ -d "$CODEX_PRMPT_DIR" ] && cp "$GOV_CMD_DIR/$cmd_name.md" "$CODEX_PRMPT_DIR/$cmd_name.md"
    fi
}

mkdir -p "$CLAUDE_CMD_DIR" "$OPENCODE_CMD_DIR" "$CODEX_PRMPT_DIR"

sync_cmd "gov-context"
sync_cmd "gov-writeback"

echo "Sync complete."
