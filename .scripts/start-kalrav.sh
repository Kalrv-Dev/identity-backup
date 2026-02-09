#!/bin/bash
# Kalrav Startup Script - Index memory, then start OpenClaw

echo "🔱 Kalrav Awakening..."

# Re-index memory files
echo "📚 Indexing memory..."
python3 ~/.openclaw/workspace/.scripts/vector_memory.py index 2>/dev/null

# Start OpenClaw TUI
echo "🚀 Starting OpenClaw..."
openclaw tui
