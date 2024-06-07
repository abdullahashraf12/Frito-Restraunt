from django.contrib import admin
from .models import Products, Category, Vendor, CardOrder, ProductImages, ProductReview, WishList, Address, Tags, UserOrderCard, Offers, ProductMealType, ProductSideDish, ProdutsAdditions, ProductAdditionsNames, ProductMealTypeNames, ProductSideDishNames, OffersNames, CardOrderItems
import logging
from django.forms.models import BaseInlineFormSet
from django.utils.html import format_html

# Register your models here.
logger = logging.getLogger(__name__)
class BaseProductMealTYPEFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        # custom validation

class ProductImagesAdmin(admin.TabularInline):
    model=ProductImages



class PMealAdmin(admin.TabularInline):
    model=ProductMealType
    formset = BaseProductMealTYPEFormSet



class PeodSidedmin(admin.TabularInline):
    model=ProductSideDish
    formset = BaseProductMealTYPEFormSet



class ProdutsAdditions(admin.TabularInline):
    model=ProdutsAdditions
    formset = BaseProductMealTYPEFormSet






class CardOrderedItemsAdmin(admin.ModelAdmin):
    list_display = ["get_user_name", "uoc_prod", "user_meal_type","quantity", "MealType", "MealSideDishes", "MealAdditions","total_price_for_meal","total_price_for_MealSideDishes","total_price_for_MealAdditions","total_price_for_all"]

    def get_user_name(self, obj):
        return obj.user.username
    
    get_user_name.short_description = 'User'


class ProductMealTypeNamesAdmin(admin.ModelAdmin):
    list_display= ["product_Meal_TYPE"]
    # def get_price(self, obj):
    #     return obj.price

    # get_price.short_description = 'Price'

    # def get_image(self, obj):
    #     if obj.images:
    #         return format_html('<img src="{}" style="height: 50px;"/>', obj.images.url)
    #     return "No Image"

    # get_image.short_description = 'Image'

class ProductSideDishNamesAdmin(admin.ModelAdmin):
    list_display = ["product_SIDE_DISH", "get_price", "get_image"]
    def get_price(self, obj):
        return obj.price

    get_price.short_description = 'Price'

    def get_image(self, obj):
        if obj.images:
            return format_html('<img src="{}" style="height: 50px;"/>', obj.images.url)
        return "No Image"

    get_image.short_description = 'Image'

class ProdutsAdditionsAdmin(admin.ModelAdmin):
    list_display= ["product_additions", "get_price", "get_image"]
    def get_price(self, obj):
        return obj.price

    get_price.short_description = 'Price'

    def get_image(self, obj):
        if obj.images:
            return format_html('<img src="{}" style="height: 50px;"/>', obj.images.url)
        return "No Image"

    get_image.short_description = 'Image'

class OffersNamesdmin(admin.ModelAdmin):
    list_display= ["product_offers"]













class ProductAdmin(admin.ModelAdmin):
    exclude = ('user',)  # Exclude the user field from the admin form
    inlines = [ProductImagesAdmin,PMealAdmin,PeodSidedmin,ProdutsAdditions]
    list_display= ["user","title","product_image","price","featured","status"]

    def save_model(self, request, obj, form, change):
        # If the user field is not set, set it to the logged-in admin user
        if not obj.user:
            logger.debug(f"User field is not set. Setting it to the logged-in admin user: {request.user}")
            obj.user = request.user
        super().save_model(request, obj, form, change)

class CategoryAdmin(admin.ModelAdmin):
    list_display= ["title","category_image"]

class VendorAdmin(admin.ModelAdmin):
    list_display= ["title","image"]

class CardOrderAdmin(admin.ModelAdmin):
    list_display= ["user","price","paid_status","order_date","product_status"]

 
class ProductReviewAdmin(admin.ModelAdmin):
    list_display= ["user","product","review","rating"]

class WichListAdmin(admin.ModelAdmin):
    list_display= ["user","product","date"]

class AddressAdmin(admin.ModelAdmin):
    list_display= ["user","address","status"]
class TagsAdmin(admin.ModelAdmin):
    list_display= ["tid","title"]
class Card_items_Admin(admin.ModelAdmin):
    search_fields = ['user__email']
    list_display= ["user","uoc_prod"]
class Offers_Admin(admin.ModelAdmin):
    search_fields = ['oid',"product_offers"]
    list_display= ["oid","product_offers"]
admin.site.register(Products,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Vendor,VendorAdmin)
admin.site.register(ProductReview,ProductReviewAdmin)
admin.site.register(WishList,WichListAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Tags,TagsAdmin)
admin.site.register(UserOrderCard,Card_items_Admin)
admin.site.register(Offers,Offers_Admin)
admin.site.register(ProductMealTypeNames,ProductMealTypeNamesAdmin)
admin.site.register(ProductSideDishNames,ProductSideDishNamesAdmin)
admin.site.register(ProductAdditionsNames,ProdutsAdditionsAdmin)
admin.site.register(OffersNames,OffersNamesdmin)
admin.site.register(CardOrderItems, CardOrderedItemsAdmin)