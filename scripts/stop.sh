#!/bin/bash

# FrenchFlow Stop Script
# Stops all running FrenchFlow servers

echo "Stopping FrenchFlow servers..."

# Kill backend (Python/uvicorn)
pkill -f "uvicorn app.main:app" 2>/dev/null || true
pkill -f "python run.py" 2>/dev/null || true

# Kill frontend (Vite/Node)
pkill -f "vite" 2>/dev/null || true

echo "✓ All FrenchFlow servers stopped"
