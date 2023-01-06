from django.db import models

# Create your models here.
class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat = models.CharField(max_length=200, verbose_name='Чат айди')
    tg_message = models.TextField(verbose_name='Текст сообщения')


    def __str__(self):  # строковое значение именования моделей в админ понелей
        return self.tg_chat

