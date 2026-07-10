# Sprint 003 - Orchestrator + Research Agent

## 🎯 Descripción

Implementación del **Orchestrator** (motor central) y el **Research Agent** (primer agente funcional).

## ✨ Qué se incluye

### Event Bus 🔔
- Comunicación entre servicios
- Publicación/suscripción de eventos
- Historial de eventos
- Event types: Agent, Task, Workflow, Data

### Task Queue 📋
- Cola de tareas con prioridades
- Estados: pending, running, completed, failed
- Ejecución FIFO con sorting por prioridad
- Input/output data management

### Workflow Engine 🔄
- Definición de workflows
- Steps con configuración
- Estados: draft, active, paused, completed, failed
- Execution tracking

### Agent System 🤖
- Base de agentes con capabilities
- Tipos: research, product, marketing, analytics, ceo, developer
- Memory management
- Message history

### Research Agent 🔬
- **Primer agente funcional**
- Market analysis
- Competitor research
- Opportunity identification
- Risk assessment
- Report generation
- Integración con Knowledge Base

### Orchestrator Service 🎪
- API endpoints para workflows
- Task management
- Event history
- Agent management
- Research execution

## 📁 Estructura de Archivos

```
apps/api/
├── services/
│   ├── orchestrator/
│   │   ├── __init__.py
│   │   ├── events.py       (NEW)
│   │   ├── tasks.py        (NEW)
│   │   ├── workflows.py    (NEW)
│   │   ├── agents.py       (NEW)
│   │   └── router.py       (NEW)
│   ├── agents/
│   │   ├── __init__.py
│   │   └── research_agent.py (NEW)
│   └── ...
├── tests/
│   └── test_orchestrator.py (NEW)
└── main.py (UPDATED)
```

## 🚀 Endpoints Nuevos

### Workflows
```
POST   /api/orchestrator/workflows    - Crear workflow
```

### Tasks
```
GET    /api/orchestrator/tasks        - Listar tareas pendientes
```

### Research
```
POST   /api/orchestrator/research     - Iniciar investigación
```

### Events
```
GET    /api/orchestrator/events       - Historial de eventos
```

### Agents
```
GET    /api/orchestrator/agents       - Listar agentes disponibles
```

## 🔬 Research Agent Features

### Capabilities
1. **Market Analysis** - Análisis de mercado
2. **Competitor Analysis** - Investigación de competencia
3. **Opportunity Identification** - Identificación de oportunidades

### Report Generation
- Findings (hallazgos)
- Market size estimation
- Opportunities list
- Risk assessment
- Recommendations
- Sources

### Knowledge Base Integration
- Guarda reportes en Knowledge Base
- Marca como públicos
- Tagging automático

## 🎯 Event Types

```
agent:started          - Agente inició
agent:stopped          - Agente detenido
agent:error            - Error en agente

task:created           - Tarea creada
task:started           - Tarea iniciada
task:completed         - Tarea completada
task:failed            - Tarea falló

workflow:started       - Workflow iniciado
workflow:completed     - Workflow completado
workflow:failed        - Workflow falló

data:processed         - Datos procesados
report:generated       - Reporte generado
```

## 📊 Example: Research Workflow

```python
# 1. Create workflow
POST /api/orchestrator/workflows
{
  "name": "Market Research Workflow",
  "steps": [
    {
      "id": "research",
      "name": "Market Research",
      "agent_id": "<research-agent-id>",
      "task_type": "research",
      "next_step": "analysis"
    },
    {
      "id": "analysis",
      "name": "Analysis",
      "task_type": "analysis",
      "next_step": "report"
    },
    {
      "id": "report",
      "name": "Generate Report",
      "task_type": "generation"
    }
  ]
}

# 2. Start research
POST /api/orchestrator/research
{
  "topic": "AI Market in 2026",
  "market_segment": "Enterprise",
  "depth": "deep"
}

# Response:
{
  "status": "completed",
  "report_id": "<uuid>",
  "findings_count": 5,
  "opportunities_count": 4
}

# 3. Monitor events
GET /api/orchestrator/events

# Response:
[
  {
    "type": "agent:started",
    "source": "research_agent",
    "timestamp": "2026-07-10T18:05:00Z",
    "data": {...}
  },
  {
    "type": "task:completed",
    "source": "research_agent",
    "timestamp": "2026-07-10T18:05:30Z",
    "data": {...}
  }
]
```

## 🧪 Tests

```bash
# Test orchestrator
pytest tests/test_orchestrator.py -v

# Test specific agent
pytest tests/test_orchestrator.py::TestOrchestrator::test_get_agents -v
```

## 🔗 System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Orchestrator                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │               Event Bus                          │  │
│  │  (Communicates between all services)             │  │
│  └──────────────────────────────────────────────────┘  │
│                        ↓                                │
│  ┌──────────────────────────────────────────────────┐  │
│  │            Workflow Engine                       │  │
│  │  (Manages workflow steps and execution)          │  │
│  └──────────────────────────────────────────────────┘  │
│                        ↓                                │
│  ┌──────────────────────────────────────────────────┐  │
│  │            Task Queue                            │  │
│  │  (Priority-based task management)                │  │
│  └──────────────────────────────────────────────────┘  │
│                        ↓                                │
│  ┌──────────────────────────────────────────────────┐  │
│  │            Agent System                          │  │
│  │  ┌────────────────────────────────────────────┐  │  │
│  │  │  Research Agent                            │  │  │
│  │  │  - Market Analysis                         │  │  │
│  │  │  - Competitor Research                     │  │  │
│  │  │  - Opportunity Identification              │  │  │
│  │  └────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────┐  │  │
│  │  │  Product Agent (Sprint 004)                │  │  │
│  │  └────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────┐  │  │
│  │  │  CEO Agent (Sprint 005)                    │  │  │
│  │  └────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────┘  │
│                        ↓                                │
│  ┌──────────────────────────────────────────────────┐  │
│  │            Knowledge Base & Storage              │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

## 📈 Métricas Monitoreadas

- Event count per type
- Task completion rate
- Agent status
- Workflow execution time
- Memory usage

## 🎯 Próximos Pasos

1. **Mergear a main**
2. **Sprint 004** - Product Agent + Enhanced Dashboard
3. **Sprint 005** - CEO Agent + Multi-agent Collaboration
4. **Sprint 006** - Event persistence + Analytics

---

**¡Primer agente funcional! 🤖**
