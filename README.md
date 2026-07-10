# 🌟 Aurelia OS

**Aurelia OS** es una plataforma empresarial de código abierto para automatizar, escalar y gestionar negocios digitales mediante agentes de IA especializados.

## 🎯 Visión

Construir un sistema operativo empresarial que funcione de forma autónoma con agentes IA especializados en cada función del negocio.

## 🏗️ Arquitectura

```
Aurelia OS
├── Aurelia Studio (Productos Digitales)
├── Aurelia Academy (Cursos)
├── Aurelia Market (Marketplace)
├── Aurelia AI (Agentes)
├── Aurelia Analytics
├── Aurelia Finance
└── Aurelia Cloud
```

## 📦 Release 0.1 - Bootstrap ✅

- ✅ Monorepo completo
- ✅ Docker & Docker Compose
- ✅ FastAPI backend
- ✅ Next.js frontend
- ✅ PostgreSQL + Redis
- ✅ GitHub Actions CI/CD
- ✅ Estructura de servicios

## 🚀 Quick Start

### Requisitos
- Docker & Docker Compose
- Node.js 18+
- Python 3.11+
- Make

### Instalación

```bash
# Clonar repositorio
git clone https://github.com/pabloarza09/aurelia-studio.git
cd aurelia-studio

# Instalar dependencias
make install

# Iniciar desarrollo
make dev
```

### Primeros pasos

```bash
# Terminal 1 - Backend
cd apps/api
uvicorn main:app --reload

# Terminal 2 - Frontend
cd apps/dashboard
npm run dev

# Terminal 3 - Redis & PostgreSQL (ya están en Docker)
make up
```

- Dashboard: http://localhost:3000
- API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## 📁 Estructura del Proyecto

```
aurelia-studio/
├── apps/
│   ├── api/                 # FastAPI backend
│   ├── dashboard/           # Next.js frontend
│   └── orchestrator/        # Orquestador de workflows
├── packages/
│   ├── sdk/                 # SDK reutilizable
│   ├── ui/                  # Componentes UI
│   ├── design-system/       # Sistema de diseño
│   └── config/              # Configuraciones compartidas
├── services/
│   ├── knowledge/           # Gestión de conocimiento
│   ├── auth/                # Autenticación
│   ├── product/             # Gestión de productos
│   └── agent/               # Servicios de agentes
├── agents/
│   ├── research-agent/      # Research Agent
│   ├── product-agent/       # Product Agent
│   └── ceo-agent/           # CEO Agent
├── infrastructure/
│   ├── docker/
│   ├── kubernetes/
│   └── terraform/
└── docs/
    ├── architecture/
    ├── engineering/
    └── decisions/
```

## 🛠️ Stack Tecnológico

### Backend
- **FastAPI** - Framework web moderno y rápido
- **SQLAlchemy** - ORM para bases de datos
- **Pydantic** - Validación de datos
- **PostgreSQL** - Base de datos principal
- **Redis** - Cache y cola de mensajes

### Frontend
- **Next.js 14** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Estilos
- **shadcn/ui** - Componentes UI

### IA & Automatización
- **OpenAI Agents SDK** - Agentes de IA
- **n8n** - Automatización de workflows

### DevOps
- **Docker** - Contenedores
- **GitHub Actions** - CI/CD
- **Kubernetes** - Orquestación (roadmap)

## 📚 Documentación

- [ARCHITECTURE.md](./docs/architecture/ARCHITECTURE.md) - Arquitectura detallada
- [CONTRIBUTING.md](./CONTRIBUTING.md) - Guía de contribución
- [QUICKSTART.md](./docs/QUICKSTART.md) - Guía rápida de instalación

## 🗓️ Roadmap

### Release 0.2
- Knowledge Service completo
- Auth Service
- Product Service
- Dashboard funcional

### Release 0.3
- Orchestrator
- Event Bus
- Primer agente (Research Agent)

### Release 0.5
- Todos los servicios base
- AI Platform completa

### Release 1.0
- Plataforma lista para producción
- Escalabilidad empresarial

## 📊 Milestones

- **Foundation** (Sprints 1-10) - Núcleo de la plataforma
- **Core Services** (Sprints 11-25) - Servicios principales
- **AI Platform** (Sprints 26-45) - Agentes y memoria
- **Product Factory** (Sprints 46-65) - Producción automatizada
- **Business Platform** (Sprints 66-80) - SEO, marketing, ventas
- **Enterprise** (Sprints 81-100) - Escalabilidad y HA

## 🎯 Objetivo

**100 ventas por día** (no por año) a través de múltiples canales:
- Etsy
- Gumroad
- Payhip
- Sitio propio
- Email marketing
- Redes sociales

## 📝 Licencia

MIT License - Ver [LICENSE](./LICENSE)

## 🤝 Contribuyendo

Ver [CONTRIBUTING.md](./CONTRIBUTING.md)

---

**Construido con 💪 por Aurelia Studio**
