"""Product CRUD operations."""

from typing import List, Optional
from uuid import UUID

from sqlalchemy.orm import Session

from core.models import Product
from core.schemas import ProductCreate, ProductUpdate


def get_product(db: Session, product_id: UUID) -> Optional[Product]:
    """Get product by ID."""
    return db.query(Product).filter(Product.id == product_id).first()


def get_products(db: Session, owner_id: UUID, skip: int = 0, limit: int = 100) -> List[Product]:
    """Get all products for a user."""
    return db.query(Product).filter(Product.owner_id == owner_id).offset(skip).limit(limit).all()


def get_active_products(db: Session, skip: int = 0, limit: int = 100) -> List[Product]:
    """Get all active products."""
    return (
        db.query(Product)
        .filter(Product.status == "active")
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_product(db: Session, owner_id: UUID, product: ProductCreate) -> Product:
    """Create a new product."""
    db_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        status=product.status,
        owner_id=owner_id,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(
    db: Session, product_id: UUID, product_update: ProductUpdate
) -> Optional[Product]:
    """Update a product."""
    db_product = get_product(db, product_id)
    if not db_product:
        return None

    update_data = product_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_product, field, value)

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: UUID) -> bool:
    """Delete a product."""
    db_product = get_product(db, product_id)
    if not db_product:
        return False

    db.delete(db_product)
    db.commit()
    return True
