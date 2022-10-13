# Generated by Django 4.0.6 on 2022-07-14 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline_Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(blank=True, max_length=50, null=True, unique=True)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(blank=True, max_length=50, null=True, unique=True)),
                ('image', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('First_Name', models.TextField(blank=True, max_length=50, null=True)),
                ('Last_Name', models.TextField(blank=True, max_length=50, null=True)),
                ('Address', models.TextField(blank=True, max_length=50, null=True)),
                ('Phone_No', models.TextField(blank=True, max_length=50, null=True, unique=True)),
                ('Credit_Card_no', models.TextField(blank=True, max_length=50, null=True, unique=True)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('User_Id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Departure_Time', models.DateTimeField(auto_now_add=True)),
                ('Landing_Time', models.DateTimeField(auto_now_add=True)),
                ('Remaining_Tickets', models.IntegerField()),
                ('Airline_Company_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.airline_company')),
                ('Destination_Country_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.country')),
                ('Origin_Country_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Origin_Country_Id', to='base.country')),
            ],
        ),
        migrations.CreateModel(
            name='User_Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role_Name', models.TextField(blank=True, max_length=15, null=True, unique=True)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.TextField(blank=True, max_length=50, null=True, unique=True)),
                ('Password', models.TextField(blank=True, max_length=50, null=True)),
                ('Email', models.TextField(blank=True, max_length=50, null=True, unique=True)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('User_Role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.user_role')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Id', models.OneToOneField(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.customer')),
                ('Flight_Id', models.OneToOneField(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.flight')),
            ],
        ),
        migrations.AddField(
            model_name='airline_company',
            name='Country_Id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Country_Id', to='base.country'),
        ),
        migrations.AddField(
            model_name='airline_company',
            name='User_ID',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.TextField(blank=True, max_length=50, null=True)),
                ('Last_Name', models.TextField(blank=True, max_length=50, null=True)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('User_Id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]