# Generated by Django 4.1.4 on 2022-12-30 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0009_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя пользователя')),
                ('email', models.EmailField(blank=True, default='', max_length=254, null=True, verbose_name='Почта пользователя')),
                ('photo', models.ImageField(blank=True, upload_to='users_photo/%Y/%m/%d')),
                ('bio', models.TextField(blank=True, default='', null=True, verbose_name='Описание профиля пользователя ')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
