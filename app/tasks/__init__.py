import time

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(ignore_result=False)
def add(x, y):
    logger.info(f"Adding {x} and {y}")
    # this represents an expensive computation
    # should be mocked on tests for development, for example
    time.sleep(10)
    return x + y
