# Generated by Django 4.1.4 on 2023-02-19 18:17

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0038_alter_questions_q_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Пустое поле'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='q_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Пустое поле'),
        ),
    ]