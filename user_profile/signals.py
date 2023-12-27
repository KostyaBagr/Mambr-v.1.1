import os
import shutil
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from user_profile.models import MyUserProfile


@receiver(pre_delete, sender=MyUserProfile)
def update_cart(sender, instance, **kwargs):
    path = os.path.join(os.path.abspath(os.path.dirname('media')),
                        os.path.join('media', f'user_{instance.photo}'))
    shutil.rmtree(path)