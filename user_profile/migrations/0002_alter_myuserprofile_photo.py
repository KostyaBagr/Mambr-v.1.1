# Generated by Django 4.1.4 on 2023-01-01 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuserprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='users_photo/%Y/%m/%d'),
        ),
    ]
