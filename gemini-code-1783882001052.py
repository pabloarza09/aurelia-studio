import os
import requests
import json
import logging
from openai import OpenAI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CEO-ResearchAgent")

class ResearchAgent:
    def __init__(self):
        # Toma la API Key configurada en nuestro archivo .env central
        self.api_key = os.getenv("OPENAI_API_KEY", "mock_key_if_testing")
        self.client = OpenAI(api_key=self.api_key)
        self.backend_url = os.getenv("NEXT_PUBLIC_API_URL", "http://localhost:8000")

    def analyze_market_trends(self, niche: str) -> dict:
        """Utiliza el LLM para estructurar los requerimientos del producto de alta demanda"""
        logger.info(f"[Brain] Analizando tendencias de mercado para el nicho: {niche}...")
        
        # Simulación de llamada estructurada (Structured Outputs) de OpenAI
        prompt = f"Analiza los productos digitales más vendidos en {niche} para 2026. Devuelve un JSON con el ID del producto ideal, descripción y precio óptimo."
        
        # Simulación del payload óptimo procesado por la IA enfocado en nuestro Planner estrella
        market_data = {
            "order_id": "AUTO-TREND-2026-001",
            "platform": "Aurelia AI Scout",
            "product_id": "prod-life-planner-2026",
            "customer_email": "ceo-agent@aurelia.studio",
            "price_paid": 19.99,
            "currency": "USD"
        }
        return market_data

    def trigger_production_pipeline(self, product_data: dict):
        """Envía los datos de la tendencia detectada directamente al Webhook de la API Core"""
        endpoint = f"{self.backend_url}/api/v1/orders/webhook"
        logger.info(f"[Pipeline] Enviando nueva oportunidad comercial al Orchestrator: {product_data['product_id']}")
        
        try:
            response = requests.post(endpoint, json=product_data)
            if response.status_code == 222 or response.status_code == 202:
                logger.info("[Success] El Orchestrator ha aceptado el producto. ¡Agentes trabajando!")
            else:
                logger.warning(f"[Warning] Respuesta inesperada del backend: {response.status_code}")
        except Exception as e:
            logger.error(f"[Error] No se pudo conectar con la API Core: {e}")

if __name__ == "__main__":
    # Ejecución de prueba del Agente
    agent = ResearchAgent()
    detected_trend = agent.analyze_market_trends("iPad Digital Planners")
    agent.trigger_production_pipeline(detected_trend)