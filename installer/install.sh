#!/bin/bash
set -e

# project-context-kit installer wrapper
# This script wraps the python installer to provide a convenient one-liner.

SOURCE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/.."
TARGET_DIR="${1:-.}"

echo "[*] project-context-kit installer"

if ! command -v python3 &> /dev/null
then
    echo "[-] Error: python3 is not installed. Please install it to continue."
    exit 1
fi

python3 "$SOURCE_DIR/installer/install.py" --target "$TARGET_DIR" --source "$SOURCE_DIR"
