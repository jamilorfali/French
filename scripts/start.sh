#!/bin/bash

# FrenchFlow Start Script
# Starts both backend and frontend servers

set -e

echo "╔═══════════════════════════════════════════════════════╗"
echo "║           🇫🇷  FrenchFlow Startup  🇫🇷                 ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo ""

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Get local IP address
get_local_ip() {
    if command -v ifconfig &> /dev/null; then
        ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | head -n1
    elif command -v ip &> /dev/null; then
        ip route get 1 | awk '{print $7}' | head -n1
    else
        echo "localhost"
    fi
}

LOCAL_IP=$(get_local_ip)

echo "Starting Backend Server..."
echo "─────────────────────────"

cd "$PROJECT_DIR/backend"

# Activate virtual environment
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo "❌ Virtual environment not found. Run ./scripts/setup.sh first."
    exit 1
fi

# Start backend in background
python run.py &
BACKEND_PID=$!
echo "  ✓ Backend started (PID: $BACKEND_PID)"

# Wait for backend to start
sleep 2

echo ""
echo "Starting Frontend Server..."
echo "──────────────────────────"

cd "$PROJECT_DIR/frontend"

# Start frontend in background
npm run dev &
FRONTEND_PID=$!
echo "  ✓ Frontend started (PID: $FRONTEND_PID)"

# Wait for frontend to start
sleep 3

echo ""
echo "═══════════════════════════════════════════════════════"
echo "✅ FrenchFlow is running!"
echo ""
echo "Access the app at:"
echo "  • Local:     http://localhost:3000"
echo "  • Network:   http://${LOCAL_IP}:3000"
echo ""
echo "API Documentation:"
echo "  • Swagger:   http://localhost:8000/docs"
echo "  • ReDoc:     http://localhost:8000/redoc"
echo ""
echo "Press Ctrl+C to stop all servers"
echo "═══════════════════════════════════════════════════════"

# Handle cleanup on exit
cleanup() {
    echo ""
    echo "Shutting down servers..."
    kill $BACKEND_PID 2>/dev/null || true
    kill $FRONTEND_PID 2>/dev/null || true
    echo "  ✓ Servers stopped"
    exit 0
}

trap cleanup SIGINT SIGTERM

# Wait for processes
wait
