from celery import Celery
import requests

celery = Celery('funds', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

class CeleryConfig:
        task_create_missing_queues = True
        celery_store_errors_even_if_ignored = True
        task_store_errors_even_if_ignored = True
        task_ignore_result = False
        task_serializer = "pickle"
        result_serializer = "pickle"
        event_serializer = "json"
        accept_content = ["pickle", "application/json", "application/x-python-serialize"]
        result_accept_content = ["pickle", "application/json", "application/x-python-serialize"]
		# celery_log = get_task_logger(__name__)

celery.config_from_object(CeleryConfig)

@celery.task(name='api.funds.tasks.create_fund_celery',bind=True, autoretry_for=(Exception,), retry_kwargs={"max_retries": 5})
def create_fund_celery(self, user_id: int, amount: float):
    
    try:
        # Simulación de API de pago (puede ser Stripe, PayPal, etc.)
        response = requests.post("https://api.mockpayments.com/pay", data={"user_id": user_id, "amount": amount})
        response.raise_for_status()

        # Guardar estado en la base de datos
        # save_payment_status(user_id, "completed")
        return {"status": "success"}
    
    except requests.RequestException as e:
        # save_payment_status(user_id, "failed")
        raise self.retry(exc=e)
    