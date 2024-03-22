from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(ignore_result=False)
def add(x, y):
    import time

    logger.info(f"Adding {x} and {y}")
    time.sleep(100)
    return x + y
