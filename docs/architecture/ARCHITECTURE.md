# Arquitectura - Aurelia OS

## Visión General

Aurelia OS es una plataforma empresarial construida como un monorepo con arquitectura de microservicios orientada a eventos. El sistema está diseñado para funcionar de forma autónoma mediante agentes de IA especializados.

## Principios Arquitectónicos

1. **Monorepo** - Código unificado para múltiples aplicaciones
2. **Microservicios** - Servicios independientes y escalables
3. **Event-Driven** - Comunicación asíncrona mediante eventos
4. **AI-First** - Agentes como ciudadanos de primera clase
5. **Type-Safe** - TypeScript + Python con type hints
6. **Infrastructure as Code** - Docker + Terraform + Kubernetes

## Estructura del Monorepo

```
eurelia-studio/
├── apps/              # Aplicaciones principales
│   ├── api/           # Backend FastAPI
│   ├── dashboard/     # Frontend Next.js
│   └── orchestrator/  # Orquestador de workflows
├── packages/          # Código compartido reutilizable
│   ├── sdk/           # SDK oficial
│   ├── ui/            # Componentes UI
│   └── design-system/ # Sistema de diseño
├── services/          # Microservicios
│   ├── knowledge/     # Gestión de conocimiento
│   ├── auth/          # Autenticación
│   ├── product/       # Gestión de productos
│   └── agent/         # Servicios de agentes
├── agents/            # Agentes de IA especializados
│   ├── research-agent/
│   ├── product-agent/
│   └── ceo-agent/
└── infrastructure/    # DevOps
    ├── docker/
    ├── kubernetes/
    └── terraform/
```

## Stack Tecnológico

### Backend
- **FastAPI** - Framework web
- **SQLAlchemy** - ORM
- **PostgreSQL** - Base de datos principal
- **Redis** - Cache y eventos
- **Pydantic** - Validación

### Frontend
- **Next.js 14** - Framework React
- **TypeScript** - Type safety
- **Tailwind CSS** - Estilos
- **shadcn/ui** - Componentes

### IA & Automatización
- **OpenAI Agents SDK** - Agentes
- **n8n** - Workflows
- **LangChain** - Chains (roadmap)

### DevOps
- **Docker** - Contenedores
- **Docker Compose** - Orquestación local
- **GitHub Actions** - CI/CD
- **Kubernetes** - Orquestación prod
- **Terraform** - IaC

## Flujo de Datos

```
Client (Next.js)
    ↓
API Gateway (FastAPI)
    ↓
Services
    ├── Knowledge Service
    ├── Auth Service
    ├── Product Service
    └── Agent Service
    ↓
Database (PostgreSQL)
    ├── Events (Redis)
    └── Cache (Redis)
```

## Modelos de Dominio

### Core Entities

```python
class Product:
    id: UUID
    name: str
    description: str
    price: float
    status: ProductStatus
    created_at: datetime
    updated_at: datetime

class Agent:
    id: UUID
    name: str
    type: AgentType
    status: AgentStatus
    config: dict
    created_at: datetime

class Workflow:
    id: UUID
    name: str
    steps: List[WorkflowStep]
    status: WorkflowStatus
    created_at: datetime
```

## Fases de Desarrollo

### Fase 1: Foundation (Sprints 1-10)
- Monorepo bootstrap
- Docker & CI/CD
- Base de datos
- API base

### Fase 2: Core Services (Sprints 11-25)
- Knowledge Service
- Auth Service
- Product Service
- Dashboard funcional

### Fase 3: AI Platform (Sprints 26-45)
- Orchestrator
- Agentes especializados
- Event Bus
- Workflows

### Fase 4: Product Factory (Sprints 46-65)
- Generación automática de productos
- SEO
- Marketing automation
- Analytics

### Fase 5: Enterprise (Sprints 66-100)
- Escalabilidad
- Seguridad
- Multi-tenant
- Compliance

## Patrones y Convenciones

### Naming
- Services: `{domain}Service`
- Routers: `{resource}Router`
- Models: `{Entity}Model`
- Schemas: `{Entity}Schema`

### Error Handling
```python
class AureliaException(Exception):
    pass

class ValidationError(AureliaException):
    pass

class NotFoundError(AureliaException):
    pass
```

### Logging
```python
from loguru import logger

logger.info("Event", extra={"context": "data"})
logger.error("Error", exc_info=True)
```

## Próximos Pasos

1. **Release 0.2** - Servicios completos
2. **Release 0.3** - Primer agente funcional
3. **Release 0.5** - Plataforma core completa
4. **Release 1.0** - Producción ready
