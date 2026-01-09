#!/bin/bash

# FrenchFlow Setup Script
# This script sets up the development environment

set -e

echo "╔═══════════════════════════════════════════════════════╗"
echo "║           🇫🇷  FrenchFlow Setup Script  🇫🇷            ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo ""

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

# Check for Python
echo "Checking for Python..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
elif command -v python &> /dev/null; then
    PYTHON_CMD=python
else
    echo "❌ Python is not installed. Please install Python 3.11 or higher."
    exit 1
fi

PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "  ✓ Found Python $PYTHON_VERSION"

# Check for Node.js
echo "Checking for Node.js..."
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 18 or higher."
    exit 1
fi

NODE_VERSION=$(node --version)
echo "  ✓ Found Node.js $NODE_VERSION"

# Check for npm
echo "Checking for npm..."
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed. Please install npm."
    exit 1
fi

NPM_VERSION=$(npm --version)
echo "  ✓ Found npm $NPM_VERSION"

echo ""
echo "Setting up Backend..."
echo "─────────────────────"

cd "$PROJECT_DIR/backend"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    $PYTHON_CMD -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "  ✓ Backend dependencies installed"

echo ""
echo "Setting up Frontend..."
echo "─────────────────────"

cd "$PROJECT_DIR/frontend"

# Install Node.js dependencies
echo "Installing Node.js dependencies..."
npm install

echo "  ✓ Frontend dependencies installed"

echo ""
echo "═══════════════════════════════════════════════════════"
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Seed the database:  ./scripts/seed.sh"
echo "  2. Start the app:      ./scripts/start.sh"
echo "═══════════════════════════════════════════════════════"
