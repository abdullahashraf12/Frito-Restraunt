# Generated by Django 5.0.3 on 2024-06-09 08:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsOffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('default', models.BooleanField(default=False)),
                ('number', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ProductsOffers', to='product.products')),
                ('product_offers', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ProductsOffers', to='product.offers')),
            ],
            options={
                'verbose_name_plural': 'PRODUCTS additions',
            },
        ),
    ]