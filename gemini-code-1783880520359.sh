cd apps/api
# Si creaste el entorno virtual como sugerimos en el Makefile:
source venv/bin/bin/activate  # En Linux/Mac
# venv\Scripts\activate      # En Windows

uvicorn main:app --reload