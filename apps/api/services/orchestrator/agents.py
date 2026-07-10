"""Agent definitions and management."""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class AgentType(str, Enum):
    """Types of agents."""

    RESEARCH = "research"
    PRODUCT = "product"
    MARKETING = "marketing"
    ANALYTICS = "analytics"
    CEO = "ceo"
    DEVELOPER = "developer"


class AgentStatus(str, Enum):
    """Agent execution status."""

    IDLE = "idle"
    RUNNING = "running"
    THINKING = "thinking"
    ERROR = "error"
    OFFLINE = "offline"


class AgentCapability(BaseModel):
    """What an agent can do."""

    name: str
    description: str
    input_schema: Dict[str, Any]  # JSON schema
    output_schema: Dict[str, Any]


class Agent(BaseModel):
    """AI Agent definition."""

    id: UUID = Field(default_factory=uuid4)
    name: str
    type: AgentType
    description: str
    status: AgentStatus = AgentStatus.IDLE
    capabilities: List[AgentCapability] = Field(default_factory=list)
    model: str = "gpt-4-turbo"  # LLM model
    temperature: float = 0.7
    memory_enabled: bool = True
    memory_size: int = 10000  # tokens
    owner_id: Optional[UUID] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    last_active: Optional[datetime] = None

    class Config:
        use_enum_values = True


class AgentMessage(BaseModel):
    """Message from/to an agent."""

    id: UUID = Field(default_factory=uuid4)
    agent_id: UUID
    role: str  # user, assistant, system
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class AgentMemory:
    """Agent memory management."""

    def __init__(self, max_messages: int = 50):
        self.messages: List[AgentMessage] = []
        self.max_messages = max_messages

    def add_message(self, message: AgentMessage) -> None:
        """Add message to memory."""
        self.messages.append(message)
        # Keep only recent messages
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages :]

    def get_recent_messages(self, count: int = 10) -> List[AgentMessage]:
        """Get recent messages."""
        return self.messages[-count:]

    def clear(self) -> None:
        """Clear memory."""
        self.messages = []
