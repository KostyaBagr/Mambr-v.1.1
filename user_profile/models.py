# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse


class MyUserProfile(AbstractUser):
    # name = models.CharField('Имя пользователя', max_length=200,default='')
    email = models.EmailField(blank=True, null=True, default='', verbose_name='Почта пользователя')
    photo = models.ImageField(upload_to='users_photo/%Y/%m/%d', blank=True,null=True)
    bio = models.TextField(blank=True, null=True, default='', verbose_name='Описание профиля пользователя')

    def __str__(self):
        return self.username






