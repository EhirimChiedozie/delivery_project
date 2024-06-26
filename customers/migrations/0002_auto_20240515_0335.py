# Generated by Django 3.2.1 on 2024-05-15 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='delivery_address',
            field=models.CharField(default='Null', max_length=300),
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='phonenumber',
            field=models.CharField(default='Null', max_length=100, unique=True),
        ),
    ]
