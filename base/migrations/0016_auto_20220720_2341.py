# Generated by Django 3.2.9 on 2022-07-20 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_auto_20220720_2325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airline_company',
            old_name='user_ID',
            new_name='user_id',
        ),
        migrations.RemoveField(
            model_name='airline_company',
            name='country_ID',
        ),
        migrations.AddField(
            model_name='airline_company',
            name='country_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country_id', to='base.country'),
        ),
    ]