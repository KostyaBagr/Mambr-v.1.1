# Generated by Django 4.1.4 on 2022-12-11 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Состояние публикации'),
        ),
    ]