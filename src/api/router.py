from fastapi import APIRouter
from .v1.database_api import router as database_router
from .v1.chat_api import router as chat_router

# Main API router
api_router = APIRouter(prefix="/api/v1")

# Include all routers
api_router.include_router(database_router)
api_router.include_router(chat_router)

# Health check endpoint
@api_router.get("/health")
async def health_check():
    return {"status": "healthy", "message": "AI Assistant API is running"}