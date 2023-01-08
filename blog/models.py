from django.contrib.auth.models import User
from django.db import models
from slugify import slugify
# Create your models here
from django.urls import reverse
from user_profile.models import *
from taggit.managers import TaggableManager

class Questions(models.Model):
    """Модель для формирования вопросов"""
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='Владелец статьи',default='')
    q_name = models.CharField(max_length=255, verbose_name='Вопрос')
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='URL')  # unique= поле уникальное
    tags = TaggableManager()
    q_text = models.TextField(verbose_name='Контент',default='')
    is_published = models.BooleanField(default=True, verbose_name='Состояние публикации')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def get_absolute_url(self):
        return reverse('question', kwargs={'q_pk': self.pk})



    def __str__(self):
        return self.q_name
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ('time_create',)



class Answer(models.Model):
    post = models.ForeignKey(Questions,on_delete=models.CASCADE, related_name='comments',null=True)
    text = models.TextField(verbose_name='Ответ',default='')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    author = models.ForeignKey(MyUserProfile, on_delete=models.CASCADE,verbose_name='Автор комментария',default='')

    class Meta:
        verbose_name = 'Ответы'
        ordering = ('-created',)


    def __str__(self):
        return 'Текст ответа {} к вопросу  {}'.format(self.text, self.post)