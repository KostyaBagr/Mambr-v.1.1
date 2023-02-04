# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from django.http import request
#
# from blog.models import Answer, Questions
# from habr import settings
# from blog.models import Questions
#
#
# @receiver(post_save, sender = Answer)
# def send_email_after_answer(created, **kwargs):
#     instance = kwargs['instance']
#     if created:
#         url = instance.post.get_absolute_url()
#         print(url)
#
#         full_url = 'http://127.0.0.1:8000' + url
#         send_mail(
#             'MambrTeam',
#             f'К вашему вопросу новый ответ - {full_url}',
#             settings.EMAIL_HOST_USER,
#             [f'{instance.post.author.email}'],
#             fail_silently=False,
#         )
# @receiver(post_save, sender = Answer)
# def send_email_after_answer_to_answer(created, **kwargs):
#     instance = kwargs['instance']
#     if created:
#         url = instance.post.get_absolute_url()
#         print(url)
#
#         full_url = 'http://127.0.0.1:8000' + url
#         send_mail(
#             'MambrTeam',
#             f'Кто-то отвелит на ваш комментарий - {full_url}',
#             settings.EMAIL_HOST_USER,
#             [f'{instance.author.email}'],
#             fail_silently=False,
#         )
