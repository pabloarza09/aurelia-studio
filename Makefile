.PHONY: help install dev up down logs test lint format clean

help:
	@echo "Available commands:"
	@echo "  make install       - Install dependencies"
	@echo "  make dev           - Start development environment"
	@echo "  make up            - Start Docker containers"
	@echo "  make down          - Stop Docker containers"
	@echo "  make logs          - View container logs"
	@echo "  make test          - Run tests"
	@echo "  make lint          - Run linters"
	@echo "  make format        - Format code"
	@echo "  make clean         - Clean artifacts"
	@echo "  make db-migrate    - Run database migrations"
	@echo "  make db-seed       - Seed database"

install:
	pnpm install
	cd apps/api && pip install -r requirements.txt

dev: up
	docker-compose logs -f

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

test:
	cd apps/api && pytest tests/ -v --cov

lint:
	cd apps/api && ruff check .
	pnpm --recursive run lint

format:
	cd apps/api && ruff format .
	pnpm --recursive run format

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name node_modules -exec rm -rf {} +
	find . -type d -name .next -exec rm -rf {} +

db-migrate:
	cd apps/api && alembic upgrade head

db-seed:
	cd apps/api && python -m scripts.seed
