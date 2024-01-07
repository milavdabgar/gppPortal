# from kombu import Exchange, Queue

# CELERY_BROKER_URL = "redis://localhost:6379/1"  # or your RabbitMQ URL
# CELERY_RESULT_BACKEND = "redis://localhost:6379/2"  # or your RabbitMQ URL

# CELERY_TASK_QUEUES = (Queue("default", Exchange("default"), routing_key="default"),)

# CELERY_TASK_DEFAULT_QUEUE = "default"
# CELERY_TASK_DEFAULT_EXCHANGE_TYPE = "direct"
# CELERY_TASK_DEFAULT_ROUTING_KEY = "default"

broker_url = "redis://localhost:6379/1"
result_backend = "redis://localhost:6379/2"
timezone = "Asia/kolkata"
broker_connection_retry_on_startup = True
