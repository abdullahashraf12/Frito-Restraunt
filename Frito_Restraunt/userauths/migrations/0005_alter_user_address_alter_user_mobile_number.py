# Generated by Django 5.0.6 on 2024-06-30 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0004_user_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Address',
            field=models.CharField(default='st', max_length=2000),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile_Number',
            field=models.CharField(default='+20', max_length=2000),
        ),
    ]
