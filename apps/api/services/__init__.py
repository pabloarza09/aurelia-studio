"""Service routers initialization."""

from services.auth import router as auth_router
from services.product import router as product_router
from services.knowledge import router as knowledge_router

__all__ = ["auth_router", "product_router", "knowledge_router"]
