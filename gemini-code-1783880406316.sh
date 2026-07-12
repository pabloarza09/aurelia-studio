curl -X 'POST' \
  'http://localhost:8000/api/v1/orders/webhook' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "order_id": "ORD-2026-001",
  "platform": "Etsy",
  "product_id": "prod-life-planner-2026",
  "customer_email": "tester@aurelia.studio",
  "price_paid": 24.50,
  "currency": "USD"
}'