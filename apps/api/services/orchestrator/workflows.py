"""Workflow definitions and execution."""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class WorkflowStatus(str, Enum):
    """Workflow execution status."""

    DRAFT = "draft"
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    FAILED = "failed"


class WorkflowStep(BaseModel):
    """Single step in a workflow."""

    id: str
    name: str
    agent_id: Optional[UUID] = None
    task_type: str  # research, analysis, generation, etc
    config: Dict[str, Any] = Field(default_factory=dict)
    next_step: Optional[str] = None
    on_error: Optional[str] = None  # fallback step


class Workflow(BaseModel):
    """Workflow definition and execution."""

    id: UUID = Field(default_factory=uuid4)
    name: str
    description: Optional[str] = None
    steps: List[WorkflowStep]
    status: WorkflowStatus = WorkflowStatus.DRAFT
    owner_id: UUID
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    class Config:
        use_enum_values = True


class WorkflowExecution(BaseModel):
    """Runtime execution of a workflow."""

    id: UUID = Field(default_factory=uuid4)
    workflow_id: UUID
    status: WorkflowStatus = WorkflowStatus.ACTIVE
    current_step: str
    executed_steps: List[str] = Field(default_factory=list)
    results: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None

    class Config:
        use_enum_values = True
