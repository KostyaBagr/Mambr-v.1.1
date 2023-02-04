from django.db.models.signals import post_save
from notice.models import Notification
from user_profile.models import *
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.mail import send_mail
class Questions(models.Model):
    """Модель для формирования вопросов"""


    COMPLEXITY =[
        ('E', 'Легкий'),
        ('M', 'Средний'),
        ('D', 'Сложный'),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='Владелец статьи')
    q_name = models.CharField(max_length=255, verbose_name='Вопрос')
    tags = TaggableManager()
    difficult = models.CharField(max_length=1, choices=COMPLEXITY, default='E')
    q_text = RichTextUploadingField(blank=True, null=True)
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
    text = RichTextUploadingField(blank=True, null=True)
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

    class Meta:
        verbose_name = 'Ответы'
        ordering = ('created',)
    def __str__(self):
        return self.text



post_save.connect(Answer.user_commented_post,sender=Answer)
