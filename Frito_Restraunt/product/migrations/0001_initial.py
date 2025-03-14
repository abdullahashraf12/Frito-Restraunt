# Generated by Django 5.0.3 on 2024-06-09 08:05

import django.db.models.deletion
import product.models
import shortuuid.django_fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='cat', unique=True)),
                ('title', models.CharField(default='Food', max_length=100)),
                ('image', models.ImageField(default='category.jpg', upload_to='Category')),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='OffersNames',
            fields=[
                ('product_offers', models.CharField(default='Default', max_length=300, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProductAdditionsNames',
            fields=[
                ('product_additions', models.CharField(default='Default', max_length=500, primary_key=True, serialize=False)),
                ('price', models.FloatField(default=0.0)),
                ('images', models.ImageField(default='product.jpg', upload_to='product-images/pa')),
            ],
        ),
        migrations.CreateModel(
            name='ProductMealTypeNames',
            fields=[
                ('product_Meal_TYPE', models.CharField(default='Default', max_length=500, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSideDishNames',
            fields=[
                ('product_SIDE_DISH', models.CharField(default='Default', max_length=500, primary_key=True, serialize=False)),
                ('price', models.FloatField(default=0.0)),
                ('images', models.ImageField(default='product.jpg', upload_to='product-images/psd')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='tid', unique=True)),
                ('title', models.CharField(default='Fresh Pear', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, null=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Address',
            },
        ),
        migrations.CreateModel(
            name='CardOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default='1.99', max_digits=9999999999999)),
                ('paid_status', models.BooleanField(default=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('product_status', models.CharField(choices=[('process', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='processing', max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Cards Order',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='', unique=True)),
                ('title', models.CharField(default='Fresh Pear', max_length=100)),
                ('image', models.ImageField(default='product.jpg', upload_to=product.models.user_directory_path)),
                ('back_image', models.ImageField(default='product.jpg', upload_to=product.models.user_directory_path)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, default='1.99', max_digits=9999999999999)),
                ('old_Price', models.DecimalField(decimal_places=2, default='2.99', max_digits=9999999999999)),
                ('spescification', models.TextField(blank=True, null=True)),
                ('products_status', models.CharField(choices=[('draft', 'Draft'), ('disabled', 'Disabled'), ('in_review', 'In_Review'), ('published', 'Published')], default='in_review', max_length=30)),
                ('status', models.BooleanField(default=True)),
                ('in_stock', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=True)),
                ('sku', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='', unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='product.category')),
                ('user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars'), (6, '6 Stars'), (7, '7 Stars')], default=None)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userrev', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prodreview', to='product.products')),
            ],
            options={
                'verbose_name_plural': 'Product Reviews',
            },
        ),
        migrations.CreateModel(
            name='ProductMealType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default='product.jpg', upload_to='product-images/pmt')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('default', models.BooleanField(default=False)),
                ('number', models.PositiveIntegerField(default=0)),
                ('price', models.FloatField(default=0.0)),
                ('product_Meal_TYPE', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ProductMealTYPE', to='product.productmealtypenames')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ProductMealTYPE', to='product.products')),
            ],
            options={
                'verbose_name_plural': 'PRODUCT Meal TYPE',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default='product.jpg', upload_to='product-images')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_images', to='product.products')),
            ],
            options={
                'verbose_name_plural': 'Products images',
            },
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='off', unique=True)),
                ('gallery_image', models.ImageField(default='product.jpg', upload_to='global_/off/')),
                ('offer_image', models.ImageField(default='product.jpg', upload_to='off_/off/')),
                ('default', models.BooleanField(default=False)),
                ('product_offers', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_offers_offers', to='product.offersnames')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.products')),
            ],
        ),
        migrations.CreateModel(
            name='CardOrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_meal_type', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('MealType', models.JSONField()),
                ('MealSideDishes', models.JSONField()),
                ('MealAdditions', models.JSONField()),
                ('total_price_for_meal', models.FloatField(default=0.0)),
                ('total_price_for_MealSideDishes', models.FloatField(default=0.0)),
                ('total_price_for_MealAdditions', models.FloatField(default=0.0)),
                ('total_price_for_all', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('uoc_prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CardOrderItemsProduct', to='product.products')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSideDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('default', models.BooleanField(default=False)),
                ('number', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ProductSideDish', to='product.products')),
                ('product_SIDE_DISH', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ProductSideDish', to='product.productsidedishnames')),
            ],
            options={
                'verbose_name_plural': 'PRODUCT SIDE DISH',
            },
        ),
        migrations.CreateModel(
            name='ProdutsAdditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('default', models.BooleanField(default=False)),
                ('number', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ProdutsAdditions', to='product.products')),
                ('product_additions', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ProdutsAdditions', to='product.productadditionsnames')),
            ],
            options={
                'verbose_name_plural': 'PRODUCTS additions',
            },
        ),
        migrations.CreateModel(
            name='UserOrderCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uoc_id', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='uoc', unique=True)),
                ('qty', models.IntegerField()),
                ('weight', models.CharField(max_length=200)),
                ('uoc_prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uoc_prod', to='product.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='ven', unique=True)),
                ('title', models.CharField(default='Nestify', max_length=100)),
                ('image', models.ImageField(default='vendor.jpg', upload_to=product.models.user_directory_path)),
                ('description', models.TextField(blank=True, default='i am amazing vendor', null=True)),
                ('address', models.CharField(default='123 Main Street', max_length=100)),
                ('contact', models.CharField(default='+123 (456) 789', max_length=100)),
                ('chat_resp_time', models.CharField(default='100', max_length=100)),
                ('shipping_resp_time', models.CharField(default='100', max_length=100)),
                ('Authentic_rating', models.CharField(default='100', max_length=100)),
                ('days_return', models.CharField(default='100', max_length=100)),
                ('warrantly_period', models.CharField(default='100', max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Vendor',
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'WishList',
            },
        ),
    ]
