# Sprint 002 - Core Services

## Descripción

Implementación de los servicios base de Aurelia OS:
- **Auth Service** - Autenticación y autorización con JWT
- **Product Service** - Gestión de productos
- **Knowledge Service** - Base de conocimiento

## ✨ Incluye

### Database Layer
- ✅ Models SQLAlchemy (User, Product, Agent, KnowledgeBase)
- ✅ Database connection pooling
- ✅ Session management

### Auth Service
- ✅ User registration
- ✅ User login con JWT tokens
- ✅ Password hashing con bcrypt
- ✅ Token verification
- ✅ Protected endpoints

### Product Service
- ✅ CRUD operations (Create, Read, Update, Delete)
- ✅ List products by user
- ✅ Authorization checks
- ✅ Product filtering

### Knowledge Service
- ✅ Knowledge base CRUD
- ✅ Search functionality
- ✅ Category filtering
- ✅ Public/Private items

### Schemas & Validation
- ✅ Pydantic schemas para todos los modelos
- ✅ Request validation
- ✅ Response serialization

### Tests
- ✅ Auth service tests
- ✅ Product service tests
- ✅ Fixtures for testing

## 📋 Estructura de Archivos

```
apps/api/
├── core/
│   ├── database.py      (NEW)
│   ├── models.py        (NEW)
│   ├── schemas.py       (NEW)
├── services/
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── crud.py      (NEW)
│   │   ├── security.py  (NEW)
│   │   └── router.py    (NEW)
│   ├── product/
│   │   ├── __init__.py
│   │   ├── crud.py      (NEW)
│   │   └── router.py    (NEW)
│   ├── knowledge/
│   │   ├── __init__.py
│   │   ├── crud.py      (NEW)
│   │   └── router.py    (NEW)
│   └── __init__.py      (NEW)
├── tests/
│   ├── test_auth.py     (NEW)
│   └── test_products.py (NEW)
└── main.py              (UPDATED)
```

## 🚀 Endpoints Disponibles

### Auth
- `POST /api/auth/register` - Registrar usuario
- `POST /api/auth/login` - Login y obtener token
- `GET /api/auth/me` - Obtener info del usuario actual

### Products
- `POST /api/products/` - Crear producto
- `GET /api/products/` - Listar productos
- `GET /api/products/{id}` - Obtener producto
- `PUT /api/products/{id}` - Actualizar producto
- `DELETE /api/products/{id}` - Eliminar producto

### Knowledge
- `POST /api/knowledge/` - Crear item de conocimiento
- `GET /api/knowledge/public` - Listar items públicos
- `GET /api/knowledge/search?q=...` - Buscar
- `GET /api/knowledge/category/{category}` - Por categoría
- `GET /api/knowledge/{id}` - Obtener item
- `PUT /api/knowledge/{id}` - Actualizar item
- `DELETE /api/knowledge/{id}` - Eliminar item

## 🔐 Autenticación

Todos los endpoints protegidos requieren header:
```
Authorization: Bearer <token>
```

## 📊 Base de Datos

### Tablas
- `users` - Usuarios registrados
- `products` - Productos
- `agents` - Agentes IA
- `knowledge_base` - Base de conocimiento

## 🧪 Testing

```bash
# Ejecutar tests
make test

# Tests con cobertura
cd apps/api && pytest tests/ -v --cov
```

## 📝 Próximos Pasos

1. Mergear a `main`
2. Sprint 003 - Orchestrator y primer agente
3. Sprint 004 - Event bus y workflows

---

**Aprobado para merge cuando esté listo** ✨
