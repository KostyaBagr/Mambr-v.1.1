from django.db import models


# Create your models here.
from user_profile.models import MyUserProfile


class Notification(models.Model):
    NOTIFICATION_TYPES = ((1, 'Like'), (2, 'Comment'))
    post = models.ForeignKey('blog.Questions', on_delete=models.CASCADE, related_name="noti_post", blank=True, null=True)
    sender = models.ForeignKey(MyUserProfile, on_delete=models.CASCADE, related_name="noti_from_user")
    user = models.ForeignKey(MyUserProfile, on_delete=models.CASCADE, related_name="noti_to_user")
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
    text_preview = models.CharField(max_length=90, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)
