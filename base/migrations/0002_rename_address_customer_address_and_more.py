# Generated by Django 4.0.6 on 2022-07-15 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Credit_Card_no',
            new_name='credit_Card_no',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='First_Name',
            new_name='first_Name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Last_Name',
            new_name='last_Name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Phone_No',
            new_name='phone_No',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='User_Id',
            new_name='user_Id',
        ),
        migrations.RenameField(
            model_name='flight',
            old_name='Airline_Company_Id',
            new_name='airline_company_id',
        ),
        migrations.RenameField(
            model_name='flight',
            old_name='Origin_Country_Id',
            new_name='origin_country_id',
        ),
    ]