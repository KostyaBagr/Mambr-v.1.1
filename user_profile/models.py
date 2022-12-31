# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.urls import reverse


class Profile(models.Model):
    """расширение модели user"""
    user = models.OneToOneField(User,unique=True,verbose_name='Пользователь', on_delete=models.CASCADE,default='')

    name = models.CharField('Имя пользователя',max_length=200)
    email = models.EmailField(blank=True, null=True,default='', verbose_name='Почта пользователя')
    photo = models.ImageField(upload_to='users_photo/%Y/%m/%d', blank=True)
    bio = models.TextField(blank=True, null=True, default='',verbose_name='Описание профиля пользователя ')

    def get_absolute_url(self):
        return reverse('registration', kwargs={'user_id': self.pk})

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
