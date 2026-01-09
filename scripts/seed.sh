#!/bin/bash

# FrenchFlow Database Seeding Script

set -e

echo "╔═══════════════════════════════════════════════════════╗"
echo "║         🇫🇷  FrenchFlow Database Seeding  🇫🇷          ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo ""

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR/backend"

# Activate virtual environment
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo "❌ Virtual environment not found. Run ./scripts/setup.sh first."
    exit 1
fi

# Run the seeding script
python -m app.seed.seed_database

echo ""
echo "✅ Database seeding complete!"
