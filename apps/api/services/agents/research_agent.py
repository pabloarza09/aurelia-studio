"""Research Agent - Market and product research."""

from datetime import datetime
from typing import Any, Dict, List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field
from loguru import logger

from services.orchestrator.agents import Agent, AgentCapability, AgentType, AgentStatus, AgentMemory, AgentMessage
from services.orchestrator.tasks import Task, TaskStatus
from services.orchestrator.events import EventType, Event, event_bus
from core.models import KnowledgeBase
from sqlalchemy.orm import Session


class ResearchTask(BaseModel):
    """Research task specification."""

    topic: str
    market_segment: Optional[str] = None
    depth: str = "standard"  # quick, standard, deep
    include_competitors: bool = True
    include_trends: bool = True


class ResearchReport(BaseModel):
    """Research report output."""

    id: UUID = Field(default_factory=uuid4)
    title: str
    topic: str
    findings: List[str]
    market_size: Optional[str] = None
    opportunities: List[str] = Field(default_factory=list)
    risks: List[str] = Field(default_factory=list)
    recommendations: List[str] = Field(default_factory=list)
    sources: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ResearchAgent:
    """Research Agent - conducts market and product research."""

    def __init__(self):
        self.agent = Agent(
            name="Research Agent",
            type=AgentType.RESEARCH,
            description="Conducts comprehensive market and product research",
            capabilities=[
                AgentCapability(
                    name="market_analysis",
                    description="Analyze market trends and sizes",
                    input_schema={"topic": "string", "market": "string"},
                    output_schema={"market_size": "string", "trends": "array"},
                ),
                AgentCapability(
                    name="competitor_analysis",
                    description="Research competing products",
                    input_schema={"product": "string"},
                    output_schema={"competitors": "array", "analysis": "string"},
                ),
                AgentCapability(
                    name="opportunity_identification",
                    description="Identify market opportunities",
                    input_schema={"market": "string", "segment": "string"},
                    output_schema={"opportunities": "array", "potential": "string"},
                ),
            ],
        )
        self.memory = AgentMemory()
        logger.info(f"Research Agent initialized: {self.agent.id}")

    async def research(self, task: ResearchTask, db: Session) -> ResearchReport:
        """Conduct research on a topic."""
        logger.info(f"Starting research: {task.topic}")

        # Update agent status
        self.agent.status = AgentStatus.RUNNING
        self.agent.last_active = datetime.utcnow()

        # Emit event
        await event_bus.publish(
            Event(
                type=EventType.AGENT_STARTED,
                source="research_agent",
                data={
                    "agent_id": str(self.agent.id),
                    "task": task.topic,
                },
            )
        )

        try:
            # Simulate research process
            findings = await self._gather_findings(task)
            opportunities = await self._identify_opportunities(task)
            risks = await self._identify_risks(task)
            recommendations = await self._generate_recommendations(task)

            report = ResearchReport(
                title=f"Research Report: {task.topic}",
                topic=task.topic,
                findings=findings,
                opportunities=opportunities,
                risks=risks,
                recommendations=recommendations,
            )

            # Save to knowledge base
            await self._save_to_knowledge_base(report, db)

            # Update agent status
            self.agent.status = AgentStatus.IDLE

            # Emit completion event
            await event_bus.publish(
                Event(
                    type=EventType.TASK_COMPLETED,
                    source="research_agent",
                    data={
                        "agent_id": str(self.agent.id),
                        "report_id": str(report.id),
                        "topic": task.topic,
                    },
                )
            )

            logger.info(f"Research completed: {task.topic}")
            return report

        except Exception as e:
            logger.error(f"Research failed: {str(e)}")
            self.agent.status = AgentStatus.ERROR

            await event_bus.publish(
                Event(
                    type=EventType.AGENT_ERROR,
                    source="research_agent",
                    data={
                        "agent_id": str(self.agent.id),
                        "error": str(e),
                    },
                )
            )
            raise

    async def _gather_findings(self, task: ResearchTask) -> List[str]:
        """Gather research findings."""
        findings = [
            f"Market for {task.topic} is growing rapidly",
            "Customer demand is increasing",
            "Competition is moderate but growing",
            "Price sensitivity varies by segment",
            "Emerging technologies are reshaping the market",
        ]
        return findings

    async def _identify_opportunities(self, task: ResearchTask) -> List[str]:
        """Identify market opportunities."""
        opportunities = [
            "First-mover advantage in emerging segments",
            "Niche market opportunities",
            "Partnership opportunities with established players",
            "Vertical integration possibilities",
        ]
        return opportunities

    async def _identify_risks(self, task: ResearchTask) -> List[str]:
        """Identify market risks."""
        risks = [
            "Rapid market saturation",
            "Large players entering the market",
            "Regulatory changes",
            "Technology disruption",
        ]
        return risks

    async def _generate_recommendations(self, task: ResearchTask) -> List[str]:
        """Generate recommendations."""
        recommendations = [
            "Focus on differentiation",
            "Build strategic partnerships",
            "Invest in R&D",
            "Consider early market entry",
        ]
        return recommendations

    async def _save_to_knowledge_base(self, report: ResearchReport, db: Session) -> None:
        """Save research report to knowledge base."""
        from core.models import KnowledgeBase

        kb_item = KnowledgeBase(
            title=report.title,
            content=f"""# {report.title}

## Findings
{chr(10).join('- ' + f for f in report.findings)}

## Opportunities
{chr(10).join('- ' + o for o in report.opportunities)}

## Risks
{chr(10).join('- ' + r for r in report.risks)}

## Recommendations
{chr(10).join('- ' + rec for rec in report.recommendations)}
""",
            category="research",
            tags=f"research,{report.topic}",
            is_public=True,
        )
        db.add(kb_item)
        db.commit()
        logger.info(f"Report saved to knowledge base: {kb_item.id}")
