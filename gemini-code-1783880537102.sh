curl -X 'POST' \
  'http://localhost:8000/api/v1/orders/webhook' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "order_id": "ORD-2026-X99",
  "platform": "Etsy",
  "product_id": "prod-life-planner-2026",
  "customer_email": "comprador.exitoso@email.com",
  "price_paid": 19.99,
  "currency": "USD"
}'