from django.contrib.auth.models import User
from django.db import models
from slugify import slugify
# Create your models here
from django.urls import reverse



class Questions(models.Model):
    """Модель для формирования вопросов"""
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Владелец статьи', blank=True, null=True )
    q_name = models.CharField(max_length=255, verbose_name='Вопрос')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')  # unique= поле уникальное
    q_cat = models.ForeignKey('Category', on_delete=models.PROTECT,
                            verbose_name='Категория', null=True)  # PROTECT запрещает удалять categoty  у которых есть ссылки на Women
    q_text = models.TextField(verbose_name='Контент',default='')
    is_published = models.BooleanField(default=True, verbose_name='Состояние публикации')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def get_absolute_url(self):
        return reverse('question', kwargs={'q_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.q_name)
        return super(Questions, self).save(*args, **kwargs)

    def __str__(self):
        return self.q_name
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ('time_create',)

class Category(models.Model):
    """Модель для формирования категорий вропросов"""
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name='Категория_вопроса')  # db_index - поиск будет выполняться быстрее
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

class Answer(models.Model):

    post = models.ForeignKey(Questions,on_delete=models.CASCADE, related_name='comments',null=True)
    text = models.TextField(verbose_name='Ответ',default='')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Автор комментария', blank=True, null=True )


    class Meta:
        verbose_name = 'Ответы'
        ordering = ('created',)


    def __str__(self):
        return 'Текст ответа {} к вопросу  {}'.format(self.text, self.post)