# Generated by Django 3.2.9 on 2022-08-25 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_user_role_try_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_role',
            name='try_time',
        ),
    ]
