# Generated by Django 5.0.6 on 2024-06-30 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_offers_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
