# Generated by Django 4.1.4 on 2023-01-27 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_alter_questions_q_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='difficult',
            field=models.ForeignKey(default='Легкий', null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.difficult', verbose_name='Сложность'),
        ),
    ]