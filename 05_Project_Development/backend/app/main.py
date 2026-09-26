import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .config import settings
from .database import engine, Base
from .routers import auth_routes, planner_routes, history_routes, page_routes

# Configure logging
logging.basicConfig(
    level=logging.INFO if not settings.DEBUG else logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("pocketsmart.app")

# Initialize database schema
Base.metadata.create_all(bind=engine)
logger.info("Database initialized successfully.")

app = FastAPI(
    title="PocketSmart AI",
    description=(
        "Intelligent Context-Aware Budget & Purchase Planning System powered by Google Gemini. "
        "Provides structured planning for Home Interiors, Parties & Events, and Wardrobe-Matched Jewelry."
    ),
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount Static Files
app.mount("/static", StaticFiles(directory=str(settings.STATIC_DIR)), name="static")

# Include Routers
app.include_router(auth_routes.router)
app.include_router(planner_routes.router)
app.include_router(history_routes.router)
app.include_router(page_routes.router)

@app.api_route("/health", methods=["GET", "HEAD"], tags=["System"])
def health_check():
    """Health and readiness check endpoint."""
    return {
        "status": "healthy",
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "gemini_configured": bool(settings.GEMINI_API_KEY and len(settings.GEMINI_API_KEY) > 5)
    }


