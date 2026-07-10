"""Event system for Aurelia OS."""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class EventType(str, Enum):
    """Event types in the system."""

    # Agent events
    AGENT_STARTED = "agent:started"
    AGENT_STOPPED = "agent:stopped"
    AGENT_ERROR = "agent:error"

    # Task events
    TASK_CREATED = "task:created"
    TASK_STARTED = "task:started"
    TASK_COMPLETED = "task:completed"
    TASK_FAILED = "task:failed"

    # Workflow events
    WORKFLOW_STARTED = "workflow:started"
    WORKFLOW_COMPLETED = "workflow:completed"
    WORKFLOW_FAILED = "workflow:failed"

    # Data events
    DATA_PROCESSED = "data:processed"
    REPORT_GENERATED = "report:generated"


class Event(BaseModel):
    """Base event model."""

    id: UUID = Field(default_factory=uuid4)
    type: EventType
    source: str  # service/agent that triggered the event
    data: Dict[str, Any]
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    correlation_id: Optional[UUID] = None  # for tracking workflows

    class Config:
        use_enum_values = True


class EventBus:
    """In-memory event bus for service communication."""

    def __init__(self):
        self.subscribers: Dict[EventType, List[callable]] = {}
        self.event_history: List[Event] = []

    def subscribe(self, event_type: EventType, handler: callable) -> None:
        """Subscribe to an event type."""
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(handler)

    def unsubscribe(self, event_type: EventType, handler: callable) -> None:
        """Unsubscribe from an event type."""
        if event_type in self.subscribers:
            self.subscribers[event_type].remove(handler)

    async def publish(self, event: Event) -> None:
        """Publish an event to all subscribers."""
        self.event_history.append(event)
        if event.type in self.subscribers:
            for handler in self.subscribers[event.type]:
                await handler(event)

    def get_history(self, limit: int = 100) -> List[Event]:
        """Get event history."""
        return self.event_history[-limit:]


# Global event bus instance
event_bus = EventBus()
