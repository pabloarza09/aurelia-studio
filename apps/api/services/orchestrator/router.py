"""Orchestrator service - manages workflows and agents."""

from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.database import get_db
from services.auth.security import get_current_user
from services.orchestrator.workflows import Workflow, WorkflowStep
from services.orchestrator.tasks import Task, task_queue
from services.orchestrator.events import event_bus, Event
from services.agents.research_agent import ResearchAgent, ResearchTask, ResearchReport
from pydantic import BaseModel
from loguru import logger

router = APIRouter(prefix="/orchestrator", tags=["orchestrator"])

# Initialize agents
research_agent = ResearchAgent()


class WorkflowCreate(BaseModel):
    """Create workflow request."""

    name: str
    description: Optional[str] = None
    steps: List[WorkflowStep]


class WorkflowResponse(BaseModel):
    """Workflow response."""

    id: UUID
    name: str
    description: Optional[str]
    status: str
    steps_count: int

    class Config:
        from_attributes = True


class TaskResponse(BaseModel):
    """Task response."""

    id: UUID
    name: str
    status: str
    priority: int

    class Config:
        from_attributes = True


@router.post("/workflows", response_model=WorkflowResponse, status_code=status.HTTP_201_CREATED)
async def create_workflow(
    workflow: WorkflowCreate,
    current_user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create a new workflow."""
    new_workflow = Workflow(
        name=workflow.name,
        description=workflow.description,
        steps=workflow.steps,
        owner_id=UUID(current_user_id),
    )
    logger.info(f"Workflow created: {new_workflow.id}")
    return WorkflowResponse(
        id=new_workflow.id,
        name=new_workflow.name,
        description=new_workflow.description,
        status=new_workflow.status,
        steps_count=len(new_workflow.steps),
    )


@router.get("/tasks", response_model=List[TaskResponse])
async def get_pending_tasks(
    current_user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get pending tasks."""
    pending = task_queue.get_pending_tasks()
    return [
        TaskResponse(id=t.id, name=t.name, status=t.status, priority=t.priority)
        for t in pending
    ]


@router.post("/research", response_model=dict, status_code=status.HTTP_201_CREATED)
async def start_research(
    request: dict,
    current_user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Start a research task."""
    try:
        task = ResearchTask(
            topic=request.get("topic"),
            market_segment=request.get("market_segment"),
            depth=request.get("depth", "standard"),
        )

        logger.info(f"Starting research for: {task.topic}")

        report = await research_agent.research(task, db)

        return {
            "status": "completed",
            "report_id": str(report.id),
            "title": report.title,
            "findings_count": len(report.findings),
            "opportunities_count": len(report.opportunities),
        }
    except Exception as e:
        logger.error(f"Research failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


@router.get("/events")
async def get_events(
    limit: int = 100,
    current_user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get event history."""
    events = event_bus.get_history(limit)
    return [
        {
            "id": str(e.id),
            "type": e.type,
            "source": e.source,
            "timestamp": e.timestamp.isoformat(),
            "data": e.data,
        }
        for e in events
    ]


@router.get("/agents")
async def get_agents(
    current_user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get available agents."""
    return [
        {
            "id": str(research_agent.agent.id),
            "name": research_agent.agent.name,
            "type": research_agent.agent.type,
            "status": research_agent.agent.status,
            "capabilities": [
                {"name": c.name, "description": c.description}
                for c in research_agent.agent.capabilities
            ],
        }
    ]
