from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet
from django.utils.html import format_html
from .models import (Products, Category, Vendor, CardOrder, ProductImages, ProductReview, WishList, Address, Tags, 
                     UserOrderCard, Offers, ProductMealType, ProductSideDish, ProdutsAdditions, ProductAdditionsNames, 
                     ProductMealTypeNames, ProductSideDishNames, OffersNames, CardOrderItems, ProductsOffers,CashierTable)
import logging

# Register your models here.
logger = logging.getLogger(__name__)

from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError




class BaseProductMealTYPEFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        check_offer
class check_offer(BaseInlineFormSet):
    def clean(self):
        super().clean()
        default_count = 0

        for form in self.forms:
            if hasattr(form, 'cleaned_data') and form.cleaned_data.get('default'):
                default_count += 1

            if default_count > 1:
                if hasattr(form, 'instance') and isinstance(form.instance, ProductsOffers):
                    raise ValidationError("Only one default offer is allowed per product.")

        if default_count > 1:
            raise ValidationError("Only one default offer is allowed per product.")
class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class PMealAdmin(admin.TabularInline):
    model = ProductMealType
    formset = BaseProductMealTYPEFormSet

class PeodSidedmin(admin.TabularInline):
    model = ProductSideDish
    formset = BaseProductMealTYPEFormSet

class ProdutsAdditions(admin.TabularInline):
    model = ProdutsAdditions
    formset = BaseProductMealTYPEFormSet

class OffersOption(admin.TabularInline):
    model = ProductsOffers
    formset = check_offer

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.request = request
        return formset

class CardOrderedItemsAdmin(admin.ModelAdmin):
    list_display = ["id","get_user_name", "uoc_prod", "user_meal_type", "quantity", "MealType", "MealSideDishes", "MealAdditions", "total_price_for_meal", "total_price_for_MealSideDishes", "total_price_for_MealAdditions", "product_offers", "total_price_for_all","checked_out_status"]

    def get_user_name(self, obj):
        return obj.user.username
    
    get_user_name.short_description = 'User'

class ProductMealTypeNamesAdmin(admin.ModelAdmin):
    list_display = ["product_Meal_TYPE"]

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
    list_display = ["product_additions", "get_price", "get_image"]

    def get_price(self, obj):
        return obj.price

    get_price.short_description = 'Price'

    def get_image(self, obj):
        if obj.images:
            return format_html('<img src="{}" style="height: 50px;"/>', obj.images.url)
        return "No Image"

    get_image.short_description = 'Image'

class OffersNamesdmin(admin.ModelAdmin):
    list_display = ["product_offers"]

class ProductAdmin(admin.ModelAdmin):
    exclude = ('user',)  # Exclude the user field from the admin form
    inlines = [ProductImagesAdmin, PMealAdmin, PeodSidedmin, ProdutsAdditions, OffersOption]
    list_display = ["user", "title", "product_image", "price", "featured", "status"]

    def save_model(self, request, obj, form, change):
        # If the user field is not set, set it to the logged-in admin user
        if not obj.user:
            logger.debug(f"User field is not set. Setting it to the logged-in admin user: {request.user}")
            obj.user = request.user
        super().save_model(request, obj, form, change)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "category_image"]

class VendorAdmin(admin.ModelAdmin):
    list_display = ["title", "image"]

class CardOrderAdmin(admin.ModelAdmin):
    list_display = ["user", "price", "paid_status", "order_date", "product_status"]

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "review", "rating"]

class WichListAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "date"]

class AddressAdmin(admin.ModelAdmin):
    list_display = ["user", "address", "status"]

class TagsAdmin(admin.ModelAdmin):
    list_display = ["tid", "title"]

class Card_items_Admin(admin.ModelAdmin):
    search_fields = ['user__email']
    list_display = ["user", "uoc_prod"]

class Offers_Admin(admin.ModelAdmin):
    search_fields = ['oid', "product_offers"]
    list_display = ["oid", "product_offers"]


# class CasherOrderItemsAdmin(admin.ModelAdmin):
#     search_fields = ['client__username', 'SalesRep__username', 'client_status']  # Adjust fields based on your actual model structure
    
#     list_display = [
#         "order_number",
#         "order_date",
#         "client",
#         "address",
#         "client_number",
#         "total_price",
#         "client_status",
#         "SalesRep"
#     ]
    
#     def get_search_results(self, request, queryset, search_term):
#         queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        
#         try:
#             # Filter by client name
#             queryset |= self.model.objects.filter(client__username__icontains=search_term)
            
#             # Filter by SalesRep name
#             queryset |= self.model.objects.filter(SalesRep__username__icontains=search_term)
            
#         except (TypeError, ValueError):
#             pass  # Handle errors if any
        
#         return queryset, use_distinct






# admin.py
from django.contrib import admin
from .models import CashierTable
            # f'<a href={obj.get_popup_url()}>Hello</a>'

class CasherOrderItemsAdmin(admin.ModelAdmin):
    search_fields = ['client__username', 'SalesRep__username', 'client_status']
    
    list_display = [
        "order_number",
        "order_date",
        "client",
        "address",
        "client_number",
        "total_price",
        "client_status",
        "SalesRep",
        "open_popup_button"  # Custom method for the button
    ]
    
    def open_popup_button(self, obj):
        if obj.client.email:
            return format_html(
                f"""
                <a href="#popupVideo" data-rel="popup" data-position-to="window" class="ui-btn ui-corner-all ui-shadow ui-btn-inline">Open Client Data</a>
<div data-role="popup" id="popupVideo" data-overlay-theme="b" data-theme="a" data-tolerance="15,15" class="ui-content">
    <iframe src="/core/user_ordered_items/{obj.client.email}" width="497" height="298" seamless=""></iframe>
</div>"""
                # email=obj.client.email
            )
        else:
            return "No email available"  # Handle case where email is None or empty
    



    open_popup_button.short_description = 'Open Client Data'  # Set the column header text
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        
        try:
            # Filter by client name
            queryset |= self.model.objects.filter(client__username__icontains=search_term)
            
            # Filter by SalesRep name
            queryset |= self.model.objects.filter(SalesRep__username__icontains=search_term)
            
        except (TypeError, ValueError):
            pass  # Handle errors if any
        
        return queryset, use_distinct
    class Media:
        css= ("/static/admin/css/admin_button_client.css")
        js = ("/static/assets/js/vendor/jquery-3.6.0.min.js",'/static/admin/js/open_popup.js',)


















admin.site.register(Products, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(WishList, WichListAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(UserOrderCard, Card_items_Admin)
admin.site.register(Offers, Offers_Admin)
admin.site.register(ProductMealTypeNames, ProductMealTypeNamesAdmin)
admin.site.register(ProductSideDishNames, ProductSideDishNamesAdmin)
admin.site.register(ProductAdditionsNames, ProdutsAdditionsAdmin)
admin.site.register(OffersNames, OffersNamesdmin)
admin.site.register(CardOrderItems, CardOrderedItemsAdmin)
admin.site.register(CashierTable, CasherOrderItemsAdmin)















# from django.contrib import admin
# from .models import Products, Category, Vendor, CardOrder, ProductImages, ProductReview, WishList, Address, Tags, UserOrderCard, Offers, ProductMealType, ProductSideDish, ProdutsAdditions, ProductAdditionsNames, ProductMealTypeNames, ProductSideDishNames, OffersNames, CardOrderItems , ProductsOffers
# import logging
# from django.forms.models import BaseInlineFormSet
# from django.utils.html import format_html

# # Register your models here.
# logger = logging.getLogger(__name__)
# class BaseProductMealTYPEFormSet(BaseInlineFormSet):
#     def clean(self):
#         super().clean()
#         # custom validation

# class ProductImagesAdmin(admin.TabularInline):
#     model=ProductImages



# class PMealAdmin(admin.TabularInline):
#     model=ProductMealType
#     formset = BaseProductMealTYPEFormSet



# class PeodSidedmin(admin.TabularInline):
#     model=ProductSideDish
#     formset = BaseProductMealTYPEFormSet



# class ProdutsAdditions(admin.TabularInline):
#     model=ProdutsAdditions
#     formset = BaseProductMealTYPEFormSet


# class OffersOption(admin.TabularInline):
#     model=ProductsOffers
#     formset = BaseProductMealTYPEFormSet






# class CardOrderedItemsAdmin(admin.ModelAdmin):
#     list_display = ["get_user_name", "uoc_prod", "user_meal_type","quantity", "MealType", "MealSideDishes", "MealAdditions","total_price_for_meal","total_price_for_MealSideDishes","total_price_for_MealAdditions","product_offers","total_price_for_all"]

#     def get_user_name(self, obj):
#         return obj.user.username
    
#     get_user_name.short_description = 'User'


# class ProductMealTypeNamesAdmin(admin.ModelAdmin):
#     list_display= ["product_Meal_TYPE"]
#     # def get_price(self, obj):
#     #     return obj.price
#     # get_price.short_description = 'Price'
#     # def get_image(self, obj):
#     #     if obj.images:
#     #         return format_html('<img src="{}" style="height: 50px;"/>', obj.images.url)
#     #     return "No Image"
#     # get_image.short_description = 'Image'

# class ProductSideDishNamesAdmin(admin.ModelAdmin):
#     list_display = ["product_SIDE_DISH", "get_price", "get_image"]
#     def get_price(self, obj):
#         return obj.price

#     get_price.short_description = 'Price'

#     def get_image(self, obj):
#         if obj.images:
#             return format_html('<img src="{}" style="height: 50px;"/>', obj.images.url)
#         return "No Image"

#     get_image.short_description = 'Image'

# class ProdutsAdditionsAdmin(admin.ModelAdmin):
#     list_display= ["product_additions", "get_price", "get_image"]
#     def get_price(self, obj):
#         return obj.price

#     get_price.short_description = 'Price'

#     def get_image(self, obj):
#         if obj.images:
#             return format_html('<img src="{}" style="height: 50px;"/>', obj.images.url)
#         return "No Image"

#     get_image.short_description = 'Image'

# class OffersNamesdmin(admin.ModelAdmin):
#     list_display= ["product_offers"]













# class ProductAdmin(admin.ModelAdmin):
#     exclude = ('user',)  # Exclude the user field from the admin form
#     inlines = [ProductImagesAdmin,PMealAdmin,PeodSidedmin,ProdutsAdditions,OffersOption]
#     list_display= ["user","title","product_image","price","featured","status"]

#     def save_model(self, request, obj, form, change):
#         # If the user field is not set, set it to the logged-in admin user
#         if not obj.user:
#             logger.debug(f"User field is not set. Setting it to the logged-in admin user: {request.user}")
#             obj.user = request.user
#         super().save_model(request, obj, form, change)

# class CategoryAdmin(admin.ModelAdmin):
#     list_display= ["title","category_image"]

# class VendorAdmin(admin.ModelAdmin):
#     list_display= ["title","image"]

# class CardOrderAdmin(admin.ModelAdmin):
#     list_display= ["user","price","paid_status","order_date","product_status"]

 
# class ProductReviewAdmin(admin.ModelAdmin):
#     list_display= ["user","product","review","rating"]

# class WichListAdmin(admin.ModelAdmin):
#     list_display= ["user","product","date"]

# class AddressAdmin(admin.ModelAdmin):
#     list_display= ["user","address","status"]
# class TagsAdmin(admin.ModelAdmin):
#     list_display= ["tid","title"]
# class Card_items_Admin(admin.ModelAdmin):
#     search_fields = ['user__email']
#     list_display= ["user","uoc_prod"]
# class Offers_Admin(admin.ModelAdmin):
#     search_fields = ['oid',"product_offers"]
#     list_display= ["oid","product_offers"]
# admin.site.register(Products,ProductAdmin)
# admin.site.register(Category,CategoryAdmin)
# admin.site.register(Vendor,VendorAdmin)
# admin.site.register(ProductReview,ProductReviewAdmin)
# admin.site.register(WishList,WichListAdmin)
# admin.site.register(Address,AddressAdmin)
# admin.site.register(Tags,TagsAdmin)
# admin.site.register(UserOrderCard,Card_items_Admin)
# admin.site.register(Offers,Offers_Admin)
# admin.site.register(ProductMealTypeNames,ProductMealTypeNamesAdmin)
# admin.site.register(ProductSideDishNames,ProductSideDishNamesAdmin)
# admin.site.register(ProductAdditionsNames,ProdutsAdditionsAdmin)
# admin.site.register(OffersNames,OffersNamesdmin)
# admin.site.register(CardOrderItems, CardOrderedItemsAdmin)