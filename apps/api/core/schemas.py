"""Pydantic schemas for request/response validation."""

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


# ==================== User Schemas ====================


class UserBase(BaseModel):
    """Base user schema."""

    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    full_name: Optional[str] = None


class UserCreate(UserBase):
    """User creation schema."""

    password: str = Field(..., min_length=8, max_length=100)


class UserUpdate(BaseModel):
    """User update schema."""

    email: Optional[EmailStr] = None
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    full_name: Optional[str] = None


class UserResponse(UserBase):
    """User response schema."""

    id: UUID
    is_active: bool
    is_admin: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# ==================== Product Schemas ====================


class ProductBase(BaseModel):
    """Base product schema."""

    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    status: str = Field(default="draft", pattern="^(draft|active|archived)$")


class ProductCreate(ProductBase):
    """Product creation schema."""

    pass


class ProductUpdate(BaseModel):
    """Product update schema."""

    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    status: Optional[str] = Field(None, pattern="^(draft|active|archived)$")


class ProductResponse(ProductBase):
    """Product response schema."""

    id: UUID
    owner_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# ==================== Agent Schemas ====================


class AgentBase(BaseModel):
    """Base agent schema."""

    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    type: str = Field(..., min_length=1, max_length=50)
    status: str = Field(default="inactive", pattern="^(active|inactive|error)$")
    config: Optional[str] = None


class AgentCreate(AgentBase):
    """Agent creation schema."""

    pass


class AgentUpdate(BaseModel):
    """Agent update schema."""

    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    type: Optional[str] = Field(None, min_length=1, max_length=50)
    status: Optional[str] = Field(None, pattern="^(active|inactive|error)$")
    config: Optional[str] = None


class AgentResponse(AgentBase):
    """Agent response schema."""

    id: UUID
    owner_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# ==================== Knowledge Base Schemas ====================


class KnowledgeBaseBase(BaseModel):
    """Base knowledge base schema."""

    title: str = Field(..., min_length=1, max_length=255)
    content: str = Field(..., min_length=1)
    category: Optional[str] = None
    tags: Optional[str] = None
    source: Optional[str] = None
    is_public: bool = False


class KnowledgeBaseCreate(KnowledgeBaseBase):
    """Knowledge base creation schema."""

    pass


class KnowledgeBaseUpdate(BaseModel):
    """Knowledge base update schema."""

    title: Optional[str] = Field(None, min_length=1, max_length=255)
    content: Optional[str] = Field(None, min_length=1)
    category: Optional[str] = None
    tags: Optional[str] = None
    source: Optional[str] = None
    is_public: Optional[bool] = None


class KnowledgeBaseResponse(KnowledgeBaseBase):
    """Knowledge base response schema."""

    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
