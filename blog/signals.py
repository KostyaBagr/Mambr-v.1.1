from django.db.models.signals import post_save

from blog.models import Answer
from django.http import HttpResponse

from django.dispatch import receiver

from user_profile.models import MyUserProfile


@receiver(post_save,sender=Answer)
def post_save_answer(created,**kwargs):
    instance = kwargs['instance']
    if created:
        print('okey')
        return HttpResponse(f'комментарий был к {instance.post}добавлен')
    else:
        return None




