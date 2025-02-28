from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.safestring import mark_safe
from userauths.models import User
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date,datetime
from django.db.models.signals import pre_save

# Create your models here.

STATUS_CHOICE = (
    ("process","Processing"),
    ("shipped","Shipped"),
    ("delivered","Delivered"),
)
STATUS = (
    ("draft","Draft"),
    ("disabled","Disabled"),
    ("in_review","In_Review"),
    ("published","Published"),
)

RATING = (
    (1,"⭐★★★★★★"),
    (2,"⭐⭐★★★★★"),
    (3,"⭐⭐⭐★★★★"),
    (4,"⭐⭐⭐⭐★★★"),
    (5,"⭐⭐⭐⭐⭐★★"),
    (6,"⭐⭐⭐⭐⭐⭐★"),
    (7,"⭐⭐⭐⭐⭐⭐⭐")
)



RATING_CHOICES = [
    (1, '1 Star'),
    (2, '2 Stars'),
    (3, '3 Stars'),
    (4, '4 Stars'),
    (5, '5 Stars'),
    (6, '6 Stars'),
    (7, '7 Stars'),
]
OFFERS = [

    ("Default","Default"),
    ("Exclusive","Exclusive"),
    ("For 1 Person","For 1 Person"),
    ("For Share","For Share"),
    ("Side dishes and desserts","Side dishes and desserts"),
    ("Beverages","Beverages")
    
    ]


PRODUCT_Meal_TYPE = [

    ("Normal","Normal"),
    ("Hot","Hot"),
    ("Mix","Mix"),
    ("Single","Single"),
    ("Double","Double"),


    ]
PRODUCT_SIDE_DISH = [

    ("Normal Sized Potatos","Normal Sized Potatos"),
    ("Coleslaw Salade","Coleslaw Salade"),
    ("Cheesy Fries","Cheesy Fries"),
    ("Cheesy Fries Halibeno","Cheesy Fries Halibeno"),
    ("Risotto","Risotto"),
    ("Boom Frite Potato Fries","Boom Frite Potato Fries"),
    ("Double Boom Frite Potato Fries","Double Boom Frite Potato Fries"),

    

    ]
PRODUCTS_additions=[
      ("Chicken Strips (Normal)","Chicken Strips (Normal)"),
      ("Chicken Strips (Spicy)","Chicken Strips (Spicy)"),
      ('lettuce','lettuce'),
      ('Tomato','Tomato'),
      ('American Cheese','American Cheese'),
      ('Smoked Turkey','Smoked turkey'),
      ('Pickle','Pickle'),
      ('Garlicky','Garlicky'),
      


]
class OffersNames(models.Model):
    product_offers = models.CharField(max_length=300,default="Default",primary_key=True)
    def __str__(self):
        return str(self.product_offers)




def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)

class Category(models.Model):
    cid = ShortUUIDField(unique=True,length=10,max_length= 20,prefix="cat",alphabet="abcdefgh12345")
    title = models.CharField(max_length=100,default = "Food")
    image = models.ImageField(upload_to="Category",default="category.jpg")
    class Meta:
        verbose_name_plural = "Category"
    
    def category_image(self):
        return mark_safe("<img src='/media/%s' width='50' height ='50'/>" % (self.image))
    def __str__(self):
        return str(self.title)
        
class Vendor(models.Model):
    vid =ShortUUIDField(unique=True,length=10,max_length= 20,prefix="ven",alphabet="abcdefgh12345")
    title = models.CharField(max_length = 100,default="Nestify")
    image = models.ImageField(upload_to=user_directory_path,default="vendor.jpg")
    description = models.TextField(null=True,blank=True,default="i am amazing vendor")
    
    address = models.CharField(max_length=100,default="123 Main Street")
    contact = models.CharField(max_length=100,default="+123 (456) 789")
    chat_resp_time =models.CharField(max_length=100,default ="100")
    shipping_resp_time =models.CharField(max_length=100,default ="100")
    Authentic_rating =models.CharField(max_length=100,default ="100")
    days_return =models.CharField(max_length=100,default ="100")
    warrantly_period = models.CharField(max_length=100,default ="100")

    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    class Meta:
        verbose_name_plural = "Vendor"
    
    def category_image(self):
        return mark_safe("<img src='/media/%s' width='50' height ='50'/>" % (self.image))
    def __str__(self):
        return str(self.title)
class Tags(models.Model):
    tid =ShortUUIDField(unique=True,length=10,max_length= 20,prefix="tid",alphabet="abcdefgh12345")
    title = models.CharField(max_length = 100,default="Fresh Pear")
    class Meta:
        verbose_name_plural = "Tags"
    def __str__(self):
        return str(self.title)
    # pass



class Products(models.Model):
    exclude = ('user',)  # Exclude the user field from the admin form
    pid =ShortUUIDField(unique=True,length=10,max_length= 20,alphabet="abcdefgh12345")
    title = models.CharField(max_length = 100,default="Fresh Pear")
    image = models.ImageField(upload_to=user_directory_path,default="product.jpg")
    back_image = models.ImageField(upload_to=user_directory_path,default="product.jpg")
    description = models.TextField(null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False) 
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name="category")
    # vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True,related_name = "vendor")
    # offers = models.ForeignKey(Offers,on_delete=models.SET_NULL,null=True,related_name = "offers")

    price = models.DecimalField(max_digits=9999999999999,decimal_places = 2,default="1.99")
    old_Price = models.DecimalField(max_digits=9999999999999,decimal_places = 2,default="2.99")
    spescification = models.TextField(null=True,blank=True)
    # tags=models.ForeignKey(Tags,on_delete=models.SET_NULL,null=True,related_name="tags")
    products_status = models.CharField(choices=STATUS,max_length=30,default="in_review")
    status=models.BooleanField(default=True)
    in_stock=models.BooleanField(default=True)

    # digital=models.BooleanField(default=False)
    featured = models.BooleanField(default=True)
    sku=ShortUUIDField(unique=True,length=10,max_length= 20,alphabet="abcdefgh12345")
    date=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.title

    def get_rating_percentage(self):
        total_ratings = self.prodreview.count()
        if total_ratings == 0:
            return {
                '1_star_percentage': 0,
                '2_star_percentage': 0,
                '3_star_percentage': 0,
                '4_star_percentage': 0,
                '5_star_percentage': 0,
                '6_star_percentage': 0,
                '7_star_percentage': 0,
            }

        star_counts = {
            f'{i}_star_count': self.prodreview.filter(rating=i).count() for i in range(1, 8)
        }

        star_percentages = {
            f'{i}_star_percentage': (star_counts[f'{i}_star_count'] / total_ratings) * 100 for i in range(1, 8)
        }

        return star_percentages
    def image_url(self):
        return self.image.url

    class Meta:
        verbose_name_plural = "Products"
    
    def product_image(self):
        return mark_safe("<img src='/media/%s' width='50' height ='50'/>" % (self.image))
    def __str__(self):
        return str(self.title)
    def precentage(self):
        new_price = (100- ((self.price/self.old_Price) * 100) )
        return new_price
    def save(self, *args, **kwargs):
        if not self.pk and not self.user_id:  # If the instance is being created and user is not set
            # Set the current logged-in user as the default value
            self.user = kwargs.pop('user', None)
        super().save(*args, **kwargs)
# class Offers(models.Model):
#     oid = ShortUUIDField(unique=True,length=10,max_length= 20,prefix="off",alphabet="abcdefgh12345")
#     product_offers = models.ForeignKey(OffersNames,on_delete=models.SET_NULL,null=True,related_name="product_offers_offers")
#     gallery_image = models.ImageField(upload_to="global_/off/",default="product.jpg")
#     offer_image = models.ImageField(upload_to="off_/off/",default="product.jpg")
#     # product = models.ForeignKey(Products, on_delete=models.CASCADE)  # ForeignKey to Products
#     # default = models.BooleanField(default=False)

#     def __str__(self):
#         return str(self.product_offers)



class Offers(models.Model):
    oid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="off", alphabet="abcdefgh12345")
    product_offers = models.ForeignKey(OffersNames, on_delete=models.SET_NULL, null=True, related_name="product_offers_offers")
    gallery_image = models.ImageField(upload_to="global_/off/", default="product.jpg")
    offer_image = models.ImageField(upload_to="off_/off/", default="product.jpg")
    offer_image_welcome = models.ImageField(upload_to="off_/welcome/", default="product.jpg",null=True)

    valid_for_today = models.BooleanField(default=False)  # Field to indicate if the offer is valid only for today
    created_at = models.DateTimeField(auto_now_add=True)  # Field to store when the offer was created
    def __str__(self):
        return str(self.product_offers)

    def clean(self):
        # Check if any other offer is valid for today
        if self.valid_for_today:
            existing_offer = Offers.objects.filter(valid_for_today=True).exclude(pk=self.pk).first()
            if existing_offer:
                raise ValidationError(
                    f"There can only be one offer valid for today. The offer that is already registered is '({existing_offer.product_offers})'."
                )
            if self.offer_image_welcome == "product.jpg" or self.offer_image_welcome=="" :
                raise ValidationError("Offer image welcome must be set if the offer is valid for today.")
        super().clean()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def is_valid_today(self):
        """Check if the offer is valid for today."""
        return self.valid_for_today and self.created_at.date() == date.today()

@receiver(pre_save, sender=Offers)
def ensure_single_valid_offer(sender, instance, **kwargs):
    # Check if any other offer is valid for today before saving
    if instance.valid_for_today:
        Offers.objects.filter(valid_for_today=True).update(valid_for_today=False)        
class ProductImages(models.Model):
    images = models.ImageField(upload_to="product-images",default="product.jpg")
    product = models.ForeignKey(Products,on_delete=models.SET_NULL,null=True,related_name="p_images")
    date=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Products images"
class ProductMealTypeNames(models.Model):
    product_Meal_TYPE = models.CharField(max_length=500, default="Default", primary_key=True)

    def __str__(self):
        return str(self.product_Meal_TYPE)

class ProductMealType(models.Model):
    product_Meal_TYPE = models.ForeignKey(ProductMealTypeNames, on_delete=models.SET_NULL, null=True, related_name="ProductMealTYPE")
    product = models.ForeignKey('Products', on_delete=models.SET_NULL, null=True, related_name="ProductMealTYPE")
    images = models.ImageField(upload_to="product-images/pmt", default="product.jpg")

    date = models.DateTimeField(auto_now_add=True)
    default = models.BooleanField(default=False)
    number = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0.00)


    class Meta:
        verbose_name_plural = "PRODUCT Meal TYPE"

    # @property
    # def price(self):
    #     return self.product_Meal_TYPE.price if self.product_Meal_TYPE else None

    # @property
    # def images(self):
    #     return self.product_Meal_TYPE.images if self.product_Meal_TYPE else None

from django.db import models

class ProductSideDishNames(models.Model):
    product_SIDE_DISH = models.CharField(max_length=500, default="Default", primary_key=True)
    price = models.FloatField(default=0.00)
    images = models.ImageField(upload_to="product-images/psd", default="product.jpg")

    def __str__(self):
        return str(self.product_SIDE_DISH)

class ProductSideDish(models.Model):
    product_SIDE_DISH = models.ForeignKey(ProductSideDishNames, on_delete=models.SET_NULL, null=True, related_name="ProductSideDish")
    product = models.ForeignKey('Products', on_delete=models.SET_NULL, null=True, related_name="ProductSideDish")
    date = models.DateTimeField(auto_now_add=True)
    default = models.BooleanField(default=False)
    number = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "PRODUCT SIDE DISH"

    @property
    def price(self):
        return self.product_SIDE_DISH.price if self.product_SIDE_DISH else None

    @property
    def images(self):
        return self.product_SIDE_DISH.images if self.product_SIDE_DISH else None





from django.db import models

class ProductAdditionsNames(models.Model):
    product_additions = models.CharField(max_length=500, default="Default", primary_key=True)
    price = models.FloatField(default=0.00)
    images = models.ImageField(upload_to="product-images/pa", default="product.jpg")

    def __str__(self):
        return str(self.product_additions)

class ProdutsAdditions(models.Model):
    product_additions = models.ForeignKey(ProductAdditionsNames, on_delete=models.SET_NULL, null=True, related_name="ProdutsAdditions")
    product = models.ForeignKey('Products', on_delete=models.SET_NULL, null=True, related_name="ProdutsAdditions")
    date = models.DateTimeField(auto_now_add=True)
    default = models.BooleanField(default=False)
    number = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "PRODUCTS additions"

    @property
    def price(self):
        return self.product_additions.price if self.product_additions else None

    @property
    def images(self):
        return self.product_additions.images if self.product_additions else None












class ProductsOffers(models.Model):
    product_offers = models.ForeignKey(Offers, on_delete=models.SET_NULL, null=True, related_name="ProductsOffers")
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, related_name="Products_Offers_prod")
    date = models.DateTimeField(auto_now_add=True)
    default = models.BooleanField(default=False)
    number = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Products Offers"

    @property
    def price(self):
        return self.product_additions.price if self.product_additions else None

    @property
    def images(self):
        return self.product_additions.images if self.product_additions else None

    def save(self, *args, **kwargs):
        if self.default:
            existing_default = ProductsOffers.objects.filter(product=self.product, default=True)
            if self.pk:
                existing_default = existing_default.exclude(pk=self.pk)
            if existing_default.exists():
                message = "<span style='color: red; font-weight: bold;'>Only one default offer is allowed per product.</span>"
                raise ValidationError(format_html(message))
        super().save(*args, **kwargs)













class CardOrder(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9999999999999,decimal_places = 2,default="1.99")
    paid_status = models.BooleanField(default=False)
    order_date=models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE,max_length=30,default="processing")
    class Meta:
        verbose_name_plural = "Cards Order"
    
# class CardOrderItems(models.Model): 
#     order = models.ForeignKey(CardOrder,on_delete=models.CASCADE)
#     invoice_no = models.CharField(max_length=200)
#     product_status= models.CharField(max_length=200)
#     item=models.CharField(max_length=200)
#     image=models.CharField(max_length=200)
#     qty=models.IntegerField()
#     price = models.DecimalField(max_digits=9999999999999,decimal_places = 2,default="1.99")
#     total = models.DecimalField(max_digits=9999999999999,decimal_places = 2,default="1.99")
#     class Meta:
#         verbose_name_plural = "Cards Order Items"
    
#     def order_image(self):
#         return mark_safe("<img src='/media/%s' width='50' height ='50'/>" % (self.image))










class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userrev")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="prodreview")
    review = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        return str(self.product.title)














class WishList(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    product= models.ForeignKey(Products,on_delete=models.CASCADE)
    date= models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "WishList"
    
    def __str__(self):
        return str(self.product.title)
class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length = 100,null=True)
    status= models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Address"
class UserOrderCard(models.Model):
    uoc_id = ShortUUIDField(unique=True, length=10, max_length=20, prefix="uoc", alphabet="abcdefgh12345", default=ShortUUIDField.generated)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    uoc_prod=models.ForeignKey(Products,on_delete=models.CASCADE,related_name="uoc_prod")
    qty=models.IntegerField()
    weight=models.CharField(max_length=200)
    def __str__(self):
        return self.user.email
default_order=[
    ("Default","Default"),
    ("Special Order","Special Order")
]
class CardOrderItems(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    uoc_prod=models.ForeignKey(Products,on_delete=models.CASCADE,related_name="CardOrderItemsProduct")
    user_meal_type=models.CharField(max_length=200) # DEFAULT OR Special Order
    quantity =models.IntegerField()
    MealType = models.JSONField() 
    MealSideDishes = models.JSONField() 
    MealAdditions = models.JSONField() 
    total_price_for_meal=models.FloatField(default=0.00)
    total_price_for_MealSideDishes=models.FloatField(default=0.00)
    total_price_for_MealAdditions=models.FloatField(default=0.00)
    total_price_for_all=models.FloatField(default=0.00)
    product_offers = models.ForeignKey(Offers, on_delete=models.SET_NULL, null=True, related_name="Products_Offers")
    checked_out_status = models.BooleanField(default=False)
    order_number = models.IntegerField(default=0)
    order_date = models.DateTimeField(default=timezone.now)

CLIENT_ORDER_STATUS = [

    ("New","New"),
    ("In Progress","In Progress"),
    ("On Delivery","On Delivery"),
    ("Finished","Finished"),


    ]
class CashierTable(models.Model):
    order_number = models.IntegerField(default=0)
    order_date = models.DateTimeField(default=timezone.now)
    client = models.ForeignKey(User,on_delete=models.CASCADE,related_name="client")
    address = models.CharField(max_length=2000)
    client_number = models.CharField(max_length=50)
    total_price = models.FloatField(default=0.00)
    client_status = models.CharField(choices=CLIENT_ORDER_STATUS,max_length=30,default="New")
    SalesRep = models.ForeignKey(User,on_delete=models.CASCADE,related_name="sale_rep",default=None, null=True)
    latitude = models.CharField(max_length=100,default=0.0)
    longitude = models.CharField(max_length=100,default=0.0)
    client_status_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Update client_status_date only when client_status field changes
        if self.pk is not None:
            original = CashierTable.objects.get(pk=self.pk)
            if original.client_status != self.client_status:
                self.client_status_date = timezone.now()
        super(CashierTable, self).save(*args, **kwargs)

    def get_popup_url(self):
        # Define logic to return the URL for the popup iframe
        print(self.client.email)
        return f'/core/user_ordered_items/{self.client.email}/{self.order_number}/'

@receiver(post_save, sender=CashierTable)
def update_related_order(sender, instance, created, **kwargs):
    if created:
        # Update related order in some way
        print("row has been created")
        pass  