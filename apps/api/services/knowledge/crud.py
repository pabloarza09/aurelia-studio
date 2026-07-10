"""Knowledge base CRUD operations."""

from typing import List, Optional
from uuid import UUID

from sqlalchemy.orm import Session

from core.models import KnowledgeBase
from core.schemas import KnowledgeBaseCreate, KnowledgeBaseUpdate


def get_knowledge_item(db: Session, item_id: UUID) -> Optional[KnowledgeBase]:
    """Get knowledge base item by ID."""
    return db.query(KnowledgeBase).filter(KnowledgeBase.id == item_id).first()


def get_knowledge_by_category(
    db: Session, category: str, skip: int = 0, limit: int = 100
) -> List[KnowledgeBase]:
    """Get knowledge items by category."""
    return (
        db.query(KnowledgeBase)
        .filter(KnowledgeBase.category == category)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_public_knowledge(
    db: Session, skip: int = 0, limit: int = 100
) -> List[KnowledgeBase]:
    """Get all public knowledge items."""
    return (
        db.query(KnowledgeBase)
        .filter(KnowledgeBase.is_public == True)
        .offset(skip)
        .limit(limit)
        .all()
    )


def search_knowledge(
    db: Session, query: str, skip: int = 0, limit: int = 100
) -> List[KnowledgeBase]:
    """Search knowledge base."""
    return (
        db.query(KnowledgeBase)
        .filter(
            (KnowledgeBase.title.ilike(f"%{query}%"))
            | (KnowledgeBase.content.ilike(f"%{query}%"))
        )
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_knowledge_item(
    db: Session, knowledge: KnowledgeBaseCreate
) -> KnowledgeBase:
    """Create a new knowledge base item."""
    db_item = KnowledgeBase(
        title=knowledge.title,
        content=knowledge.content,
        category=knowledge.category,
        tags=knowledge.tags,
        source=knowledge.source,
        is_public=knowledge.is_public,
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_knowledge_item(
    db: Session, item_id: UUID, knowledge_update: KnowledgeBaseUpdate
) -> Optional[KnowledgeBase]:
    """Update a knowledge base item."""
    db_item = get_knowledge_item(db, item_id)
    if not db_item:
        return None

    update_data = knowledge_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_item, field, value)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_knowledge_item(db: Session, item_id: UUID) -> bool:
    """Delete a knowledge base item."""
    db_item = get_knowledge_item(db, item_id)
    if not db_item:
        return False

    db.delete(db_item)
    db.commit()
    return True
