# Generated by Django 5.0.3 on 2024-06-06 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_remove_productmealtype_images_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productadditionsnames',
            name='images',
        ),
        migrations.RemoveField(
            model_name='productmealtypenames',
            name='images',
        ),
        migrations.RemoveField(
            model_name='productsidedishnames',
            name='images',
        ),
        migrations.AddField(
            model_name='productmealtype',
            name='images',
            field=models.ImageField(default='product.jpg', upload_to='product-images/pmt'),
        ),
        migrations.AddField(
            model_name='productsidedish',
            name='images',
            field=models.ImageField(default='product.jpg', upload_to='product-images/psd'),
        ),
        migrations.AddField(
            model_name='produtsadditions',
            name='images',
            field=models.ImageField(default='product.jpg', upload_to='product-images/pa'),
        ),
    ]