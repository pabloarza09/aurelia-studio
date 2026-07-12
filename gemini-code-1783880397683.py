from fastapi import FastAPI, HTTPException, BackgroundTasks, Status
from pydantic import BaseModel, Field
from typing import Dict, Any
import logging

# Configuración de logs para auditoría de los Agentes
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AureliaOS-Core")

app = FastAPI(
    title="Aurelia OS - API Core",
    version="0.1.0",
    description="Motor de automatización y orquestación para agentes de IA de Aurelia Studio"
)

# Esquema de datos estricto para recibir compras (Etsy, Gumroad, Payhip)
class WebhookOrder(BaseModel):
    order_id: str = Field(..., example="ORD-2026-99411")
    platform: str = Field(..., example="Etsy")
    product_id: str = Field(..., example="prod-life-planner-2026")
    customer_email: str = Field(..., example="cliente@email.com")
    price_paid: float = Field(..., example=19.99)
    currency: str = Field(default="USD", example="USD")

# Tarea en segundo plano (Background Task) gestionada asíncronamente
def orchestrate_agent_workflow(order: WebhookOrder):
    """
    Simula la interacción del Monorepo:
    1. Redis encola la petición.
    2. El Orchestrator valida con knowledge-service.
    3. El agent-service envía el producto al cliente de forma autónoma.
    """
    logger.info(f"[Orchestrator] Procesando orden {order.order_id} desde {order.platform}")
    
    # Simulación de lógica de servicios
    logger.info(f"[Knowledge-Service] Verificando permisos para el recurso: {order.product_id}")
    logger.info(f"[Agent-Service] CEO Agent autorizó la transacción comercial.")
    logger.info(f"[Notification] Archivo digital enviado con éxito a {order.customer_email}")
    logger.info(f"[Aurelia Analytics] Métricas actualizadas: +{order.price_paid} {order.currency}")

@app.get("/")
def read_root():
    return {
        "status": "online",
        "ecosystem": "Aurelia OS",
        "version": "0.1-bootstrap"
    }

@app.post("/api/v1/orders/webhook", status_code=Status.HTTP_202_ACCEPTED)
async def receive_order_webhook(order: WebhookOrder, background_tasks: BackgroundTasks):
    """
    Endpoint estratégico que recibe las ventas multicanal en tiempo real.
    No bloquea al cliente externo; procesa todo de forma asíncrona mediante agentes.
    """
    logger.info(f"Webhook recibido con éxito de {order.platform}. ID de Orden: {order.order_id}")
    
    # Delegamos la ejecución pesada a las colas asíncronas del sistema
    background_tasks.add_task(orchestrate_agent_workflow, order)
    
    return {
        "success": True,
        "message": "Orden recibida por Aurelia OS y enviada al flujo de agentes.",
        "order_tracking_id": order.order_id
    }