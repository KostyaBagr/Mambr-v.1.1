# Generated by Django 4.1.4 on 2022-12-13 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_commets'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commets',
            new_name='Comments',
        ),
    ]
