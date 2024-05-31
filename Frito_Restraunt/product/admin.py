from django.contrib import admin
from .models import Products,Category,Vendor,CardOrder,CardOrderItems,ProductImages,ProductReview,WishList,Address,Tags, UserOrderCard,Offers
import logging
# Register your models here.
logger = logging.getLogger(__name__)

class ProductImagesAdmin(admin.TabularInline):
    model=ProductImages

class ProductAdmin(admin.ModelAdmin):
    exclude = ('user',)  # Exclude the user field from the admin form
    inlines = [ProductImagesAdmin]
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

class CardOrderItemsAdmin(admin.ModelAdmin):
    list_display= ["order","invoice_no","item","image","qty","price","total"]

 
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
admin.site.register(CardOrder,CardOrderAdmin)
admin.site.register(CardOrderItems,CardOrderItemsAdmin)
admin.site.register(ProductReview,ProductReviewAdmin)
admin.site.register(WishList,WichListAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Tags,TagsAdmin)
admin.site.register(UserOrderCard,Card_items_Admin)
admin.site.register(Offers,Offers_Admin)
