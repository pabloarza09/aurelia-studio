from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# En producción esto vendría de tus variables de entorno (.env)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/aurelia_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Dependencia para inyectar la sesión de la BD en los endpoints"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()