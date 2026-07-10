"""Tests for orchestrator service."""

import pytest
from fastapi.testclient import TestClient


@pytest.mark.unit
class TestOrchestrator:
    """Orchestrator service tests."""

    def test_get_agents(self, client, user_token):
        """Test getting available agents."""
        response = client.get(
            "/orchestrator/agents",
            headers={"Authorization": f"Bearer {user_token}"},
        )
        assert response.status_code == 200
        agents = response.json()
        assert len(agents) > 0
        assert agents[0]["name"] == "Research Agent"

    def test_get_events(self, client, user_token):
        """Test getting event history."""
        response = client.get(
            "/orchestrator/events",
            headers={"Authorization": f"Bearer {user_token}"},
        )
        assert response.status_code == 200
        events = response.json()
        assert isinstance(events, list)

    def test_create_workflow(self, client, user_token):
        """Test creating a workflow."""
        workflow_data = {
            "name": "Research Workflow",
            "description": "Conduct market research",
            "steps": [
                {
                    "id": "step1",
                    "name": "Market Analysis",
                    "task_type": "research",
                    "next_step": "step2",
                },
                {
                    "id": "step2",
                    "name": "Generate Report",
                    "task_type": "generation",
                },
            ],
        }
        response = client.post(
            "/orchestrator/workflows",
            json=workflow_data,
            headers={"Authorization": f"Bearer {user_token}"},
        )
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Research Workflow"
        assert data["steps_count"] == 2
