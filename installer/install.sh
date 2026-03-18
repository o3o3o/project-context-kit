#!/bin/bash
set -e

# Repo Governance Kit Installer Wrapper
# This script wraps the python installer to provide a convenient one-liner.

SOURCE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/.."
TARGET_DIR="${1:-.}"

echo "[*] Repo Governance Kit Installer"

if ! command -v python3 &> /dev/null
then
    echo "[-] Error: python3 is not installed. Please install it to continue."
    exit 1
fi

python3 "$SOURCE_DIR/installer/install.py" --target "$TARGET_DIR" --source "$SOURCE_DIR"
