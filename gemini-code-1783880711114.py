from fastapi import FastAPI, HTTPException, BackgroundTasks, Status, Depends
from sqlalchemy.orm import Session
from database import get_db, engine
import models
from pydantic import BaseModel, Field
import logging

# Crear las tablas automáticamente al iniciar (ideal para desarrollo/bootstrap)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Aurelia OS - API Core V2")
logger = logging.getLogger("AureliaOS-Core")

class WebhookOrder(BaseModel):
    order_id: str
    platform: str
    product_id: str
    customer_email: str
    price_paid: float
    currency: str = "USD"

def orchestrate_agent_workflow(order_id: str, db: Session):
    """Los agentes leen el registro guardado de la BD para procesar el flujo"""
    order = db.query(models.OrderModel).filter(models.OrderModel.id == order_id).first()
    if order:
        logger.info(f"[Orchestrator] Procesando orden {order.id} desde la BD.")
        # Aquí continúa el flujo de tus servicios...

@app.post("/api/v1/orders/webhook", status_code=Status.HTTP_202_ACCEPTED)
async def receive_order_webhook(
    order: WebhookOrder, 
    background_tasks: BackgroundTasks, 
    db: Session = Depends(get_db)
):
    logger.info(f"Insertando orden {order.order_id} en PostgreSQL...")
    
    # Guardamos el registro de forma persistente e inmediata
    db_order = models.OrderModel(
        id=order.order_id,
        platform=order.platform,
        product_id=order.product_id,
        customer_email=order.customer_email,
        price_paid=order.price_paid,
        currency=order.currency
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    
    # Pasamos el ID a la tarea en segundo plano para que los agentes trabajen de forma asíncrona
    background_tasks.add_task(orchestrate_agent_workflow, db_order.id, db)
    
    return {
        "success": True,
        "message": "Orden persistida con éxito en PostgreSQL y enviada a los agentes."
    }