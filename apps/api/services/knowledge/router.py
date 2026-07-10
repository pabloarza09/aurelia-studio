"""Knowledge base service routes."""

from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.database import get_db
from core.schemas import KnowledgeBaseCreate, KnowledgeBaseResponse, KnowledgeBaseUpdate
from services.auth.security import get_current_user
from services.knowledge.crud import (
    create_knowledge_item,
    delete_knowledge_item,
    get_knowledge_by_category,
    get_knowledge_item,
    get_public_knowledge,
    search_knowledge,
    update_knowledge_item,
)

router = APIRouter(prefix="/knowledge", tags=["knowledge"])


@router.post("/", response_model=KnowledgeBaseResponse, status_code=status.HTTP_201_CREATED)
async def create_knowledge(
    knowledge: KnowledgeBaseCreate,
    current_user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create a new knowledge base item."""
    db_item = create_knowledge_item(db, knowledge)
    return db_item


@router.get("/public", response_model=List[KnowledgeBaseResponse])
async def list_public_knowledge(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    """List all public knowledge items."""
    items = get_public_knowledge(db, skip, limit)
    return items


@router.get("/search", response_model=List[KnowledgeBaseResponse])
async def search_knowledge_endpoint(
    q: str,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    """Search knowledge base."""
    items = search_knowledge(db, q, skip, limit)
    return items


@router.get("/category/{category}", response_model=List[KnowledgeBaseResponse])
async def get_by_category(
    category: str,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    """Get knowledge items by category."""
    items = get_knowledge_by_category(db, category, skip, limit)
    return items


@router.get("/{item_id}", response_model=KnowledgeBaseResponse)
async def get_knowledge_endpoint(
    item_id: UUID,
    db: Session = Depends(get_db),
):
    """Get a knowledge item by ID."""
    item = get_knowledge_item(db, item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Knowledge item not found",
        )
    return item


@router.put("/{item_id}", response_model=KnowledgeBaseResponse)
async def update_knowledge_endpoint(
    item_id: UUID,
    knowledge_update: KnowledgeBaseUpdate,
    current_user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update a knowledge item."""
    item = get_knowledge_item(db, item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Knowledge item not found",
        )

    updated_item = update_knowledge_item(db, item_id, knowledge_update)
    return updated_item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_knowledge_endpoint(
    item_id: UUID,
    current_user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete a knowledge item."""
    item = get_knowledge_item(db, item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Knowledge item not found",
        )

    delete_knowledge_item(db, item_id)
