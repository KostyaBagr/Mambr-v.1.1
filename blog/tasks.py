from celery.decorators import task
from celery.utils.log import get_task_logger
from blog.email import send_answer_by_email

logger = get_task_logger(__name__)

@task(name='send_answer_by_email')
def send_answer_by_email(text):
    logger.info('Сообщение отправленно')
    return send_answer_by_email(text)