# Generated by Django 5.0.3 on 2024-06-22 19:25

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_cardorderitems_order_number'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CashierTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField(default=0)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('address', models.CharField(max_length=2000)),
                ('client_number', models.IntegerField()),
                ('total_price', models.FloatField(default=0.0)),
                ('client_status', models.CharField(choices=[('New', 'New'), ('In Progress', 'In Progress'), ('On Delivery', 'On Delivery'), ('Finished', 'Finished')], default='New', max_length=30)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]