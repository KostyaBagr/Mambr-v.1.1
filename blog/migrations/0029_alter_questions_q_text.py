# Generated by Django 4.1.4 on 2023-01-26 20:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_alter_answer_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='q_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
