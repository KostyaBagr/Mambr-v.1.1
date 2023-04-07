
from blog.models import  Answer
from habr import settings
from django.core.mail import send_mail

from habr.celery import app



@app.task
def send_email_after_answer():

    for i in Answer.objects.all():
        send_mail(
            'MambrTeam, новый ответ ',
            f'Коментарий к {i.post} был добавлен, вот его текст '
            f' - "{i.text}" ',
            settings.EMAIL_HOST_USER,
            [i.post.author.email],
            fail_silently=False
        )

