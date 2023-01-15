from django.db.models.signals import post_save, post_delete
from notice.models import Notification
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

    def get_answer(self):
        return self.answer_set.filter(parent__isnull=True)

    def __str__(self):
        return self.q_name
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ('time_create',)



class Answer(models.Model):
    post = models.ForeignKey(Questions,on_delete=models.CASCADE,null=True)
    text = models.TextField(verbose_name='Ответ',default='')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(MyUserProfile, on_delete=models.CASCADE,verbose_name='Автор комментария',default='')



    def user_commented_post(sender, instance, *args, **kwargs):
        answer = instance
        post = answer.post
        sender = answer.author
        text_preview = answer.text[:50]

        notify = Notification(post=post, sender=sender, user=post.author,text_preview=text_preview, notification_type=2)
        notify.save()

    def user_uncommented_post(sender, instance, *args, **kwargs):
        answer = instance
        post = answer.post

        sender = answer.author
        notify = Notification.objects.filter(post=post,author=post.author, sender=sender, user=post.author,notification_type=2)
        notify.delete()

    class Meta:
        verbose_name = 'Ответы'
        ordering = ('created',)
    def __str__(self):
        return self.text

#answer


class HelpedAnswer(models.Model):
    like_answer = models.ManyToManyField(MyUserProfile, blank=True, related_name='likes')
    dislike_answer = models.ManyToManyField(MyUserProfile, blank=True, related_name='dislikes')

    class Meta:
        verbose_name = "Правильные ответы"
    def __str__(self):
        return self.like_answer

post_save.connect(Answer.user_commented_post,sender=Answer)
post_delete.connect(Answer.user_uncommented_post,sender=Answer)