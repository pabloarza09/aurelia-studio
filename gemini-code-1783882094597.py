from fastapi import FastAPI, Status
from pydantic import BaseModel
from queue_worker import process_order_pipeline
import logging

app = FastAPI(title="Aurelia OS - API Core con Redis")
logger = logging.getLogger("AureliaOS-Core")

class WebhookOrder(BaseModel):
    order_id: str
    platform: str
    product_id: str
    customer_email: str
    price_paid: float
    currency: str = "USD"

@app.post("/api/v1/orders/webhook", status_code=Status.HTTP_202_ACCEPTED)
async def receive_order_webhook(order: WebhookOrder):
    logger.info(f"Petición recibida de {order.platform}. Enviando a la cola de Redis...")
    
    # .delay() envía la tarea a Redis instantáneamente y libera la API en milisegundos
    process_order_pipeline.delay(
        order_id=order.order_id,
        product_id=order.product_id,
        customer_email=order.customer_email
    )
    
    return {
        "success": True,
        "message": "Orden encolada en Redis. Los agentes la procesarán de forma asíncrona.",
        "order_id": order.order_id
    }