import sys
import uvicorn
from backend.app.config import settings

def main():
    print(f"==================================================")
    print(f" PocketSmart AI — Starting Application Server")
    print(f" Host: http://{settings.APP_HOST}:{settings.APP_PORT}")
    print(f" Docs: http://{settings.APP_HOST}:{settings.APP_PORT}/docs")
    print(f" Mode: {'Gemini AI Online' if settings.GEMINI_API_KEY else 'Mock Fallback Active (Offline Mode)'}")
    print(f"==================================================")

    uvicorn.run(
        "backend.app.main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.DEBUG
    )

if __name__ == "__main__":
    main()

