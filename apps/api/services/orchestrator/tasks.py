"""Task queue and job management."""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    """Task status states."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class Task(BaseModel):
    """Task in the queue."""

    id: UUID = Field(default_factory=uuid4)
    name: str
    description: Optional[str] = None
    agent_id: Optional[UUID] = None
    status: TaskStatus = TaskStatus.PENDING
    input_data: Dict[str, Any] = Field(default_factory=dict)
    output_data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    priority: int = 0  # Higher = more important
    created_at: datetime = Field(default_factory=datetime.utcnow)
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    class Config:
        use_enum_values = True


class TaskQueue:
    """Simple task queue implementation."""

    def __init__(self):
        self.tasks: Dict[UUID, Task] = {}
        self.pending_tasks: List[UUID] = []  # Priority queue

    def enqueue(self, task: Task) -> UUID:
        """Add task to queue."""
        self.tasks[task.id] = task
        self.pending_tasks.append(task.id)
        # Sort by priority (descending)
        self.pending_tasks.sort(
            key=lambda tid: self.tasks[tid].priority, reverse=True
        )
        return task.id

    def dequeue(self) -> Optional[Task]:
        """Get next task from queue."""
        if not self.pending_tasks:
            return None
        task_id = self.pending_tasks.pop(0)
        task = self.tasks[task_id]
        task.status = TaskStatus.RUNNING
        task.started_at = datetime.utcnow()
        return task

    def complete_task(self, task_id: UUID, output_data: Dict[str, Any]) -> None:
        """Mark task as completed."""
        if task_id in self.tasks:
            task = self.tasks[task_id]
            task.status = TaskStatus.COMPLETED
            task.output_data = output_data
            task.completed_at = datetime.utcnow()

    def fail_task(self, task_id: UUID, error: str) -> None:
        """Mark task as failed."""
        if task_id in self.tasks:
            task = self.tasks[task_id]
            task.status = TaskStatus.FAILED
            task.error = error
            task.completed_at = datetime.utcnow()

    def get_task(self, task_id: UUID) -> Optional[Task]:
        """Get task by ID."""
        return self.tasks.get(task_id)

    def get_pending_tasks(self) -> List[Task]:
        """Get all pending tasks."""
        return [self.tasks[tid] for tid in self.pending_tasks if tid in self.tasks]


# Global task queue
task_queue = TaskQueue()
