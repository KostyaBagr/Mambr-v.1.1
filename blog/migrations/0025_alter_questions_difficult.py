# Generated by Django 4.1.4 on 2023-01-21 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_difficult_alter_questions_difficult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='difficult',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.difficult', verbose_name='Сложность'),
        ),
    ]