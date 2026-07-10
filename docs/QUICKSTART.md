# Quick Start - Aurelia OS

## Requisitos Previos

- Docker & Docker Compose
- Node.js 18+
- Python 3.11+
- Git
- Make

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/pabloarza09/aurelia-studio.git
cd aurelia-studio
```

### 2. Configurar variables de entorno

```bash
cp .env.example .env
```

### 3. Instalar dependencias

```bash
make install
```

### 4. Levantar el stack

```bash
make up
```

## Verificar instalación

```bash
# Health check del API
curl http://localhost:8000/api/health

# Dashboard
open http://localhost:3000

# API Docs
open http://localhost:8000/docs
```

## Estructura de directorios explicada

```
.
├── apps/
│   ├── api/          # Backend Python/FastAPI
│   └── dashboard/    # Frontend TypeScript/React
├── packages/         # Librerías compartidas
├── services/         # Microservicios
├── docker-compose.yml # Orquestación local
└── Makefile         # Comandos útiles
```

## Comandos útiles

```bash
# Desarrollo
make dev           # Iniciar stack completo
make logs          # Ver logs en tiempo real

# Testing
make test          # Ejecutar tests

# Código
make format        # Formatear código
make lint          # Verificar código

# Base de datos
make db-migrate    # Ejecutar migraciones
make db-seed       # Seed de datos
```

## Problemas comunes

### Puerto 8000 ya en uso

```bash
lsof -i :8000
kill -9 <PID>
```

### Docker Compose no encuentra los servicios

```bash
make down
make up
```

### Migraciones de BD fallando

```bash
make db-migrate
```

## Próximos pasos

1. Explorar la documentación en `docs/`
2. Revisar `CONTRIBUTING.md` para desarrollar
3. Leer `docs/architecture/ARCHITECTURE.md` para entender el sistema
