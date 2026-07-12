cd apps/api
celery -A queue_worker.celery_app worker --loglevel=info