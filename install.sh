#!/bin/bash
set -e

echo "Installing Mr. Braincells..."

# Check for curl
if ! command -v curl >/dev/null 2>&1; then
    echo "curl required"
    exit 1
fi

# Install ollama if not present
if ! command -v ollama >/dev/null 2>&1; then
    echo "Installing Ollama..."
    curl -fsSL https://ollama.com/install.sh | sh
fi

echo "Done. Run: mr-braincells"
