from django.template import Context
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

#
# def send_answer_by_email(text):
#     context ={
#         'text':text
#     }
#     subject = 'Новый ответ на ваш вопрос'
#     body = render_to_string('blog/email_message.txt', context)
#     email = EmailMessage(
#         subject, body,
#         settings.EMAIL_HOST_USER,
#         ['dipkroy08@gmail.com']
#     )