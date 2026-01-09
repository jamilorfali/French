#!/usr/bin/env python3
"""
Run the FrenchFlow backend server.
"""
import uvicorn
from app.config import settings


def main():
    """Run the FastAPI application."""
    print(f"""
    ╔═══════════════════════════════════════════════════════╗
    ║           🇫🇷  FrenchFlow Backend Server  🇫🇷          ║
    ╠═══════════════════════════════════════════════════════╣
    ║  Running on: http://{settings.host}:{settings.port}               ║
    ║  API Docs:   http://localhost:{settings.port}/docs             ║
    ║  LAN Access: http://<your-mac-ip>:{settings.port}              ║
    ╚═══════════════════════════════════════════════════════╝
    """)

    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level="info",
    )


if __name__ == "__main__":
    main()
