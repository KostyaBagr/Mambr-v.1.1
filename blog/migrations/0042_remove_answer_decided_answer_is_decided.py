# Generated by Django 4.1.4 on 2023-03-08 19:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0041_answer_decided'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='decided',
        ),
        migrations.AddField(
            model_name='answer',
            name='is_decided',
            field=models.ManyToManyField(related_name='is_decided_question', to=settings.AUTH_USER_MODEL),
        ),
    ]