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
from django.http import JsonResponse, HttpResponseNotAllowed




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
    list_display = ["id","get_user_name", "uoc_prod", "user_meal_type", "quantity", "MealType", "MealSideDishes", "MealAdditions", "total_price_for_meal", "total_price_for_MealSideDishes", "total_price_for_MealAdditions", "product_offers", "total_price_for_all","checked_out_status","order_number"]

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





# from django.contrib import admin
# from django.utils.html import format_html

# class CasherOrderItemsAdmin(admin.ModelAdmin):
#     search_fields = ['client__username', 'SalesRep__username', 'client_status']
    
#     list_display = [
#         "order_number",
#         "order_date",
#         "client",
#         "address",
#         "client_number",
#         "total_price",
#         "client_status",
#         "SalesRep",
#         "open_popup_button"
#     ]
    
#     list_editable = ['client_status']
#     def open_popup_button(self, obj):
#         if obj.client.email:
#             return format_html(f"""
# <div class="popup-container">
#     <a href="#" class="openPopup ui-btn ui-corner-all ui-shadow ui-btn-inline">Open Client Data</a>
#     <div class="popup">
#         <div class="popup-content">
#             <iframe name="my_iframe" data-src="/core/user_ordered_items/{obj.client.email}" class="videoIframe" style="display: none; margin-left: -360%; margin-top: 10%;" width="450%" height="400px" seamless=""></iframe>
#         </div>
#     </div>
# </div>
#             """)
#         else:
#             return "No email available"
 
#     open_popup_button.short_description = 'Open Client Data'
    
#     def get_popup_url(self, obj):
#         # Ensure this method returns the URL string for the iframe
#         return f'/core/user_ordered_items/{obj.client.email}/'
    
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
#     class Media:
#         # css= {
#         #     'all': ("/static/admin/css/admin_button_client.css",)
#         # }
#         js = ("/static/assets/js/vendor/jquery-3.6.0.min.js", '/static/admin/js/open_popup.js')






# from django import forms
# from django.contrib import admin
# from django.utils.html import format_html
# from .models import CashierTable, User  # Import your models

# # Custom form for CasherOrderItemsAdmin
# class CashierOrderForm(forms.ModelForm):
#     class Meta:
#         model = CashierTable
#         fields = '__all__'

#     # Override SalesRep field to show only Sales Representatives
#     SalesRep = forms.ModelChoiceField(
#         queryset=User.objects.filter(client_status='Sales Representative'),
#         label='Sales Representative'
#     )

# # Define your admin class
# class CasherOrderItemsAdmin(admin.ModelAdmin):
#     search_fields = ['client__username', 'SalesRep__username', 'client_status']
    
#     list_display = [
#         "order_number",
#         "order_date",
#         "client",
#         "address",
#         "client_number",
#         "total_price",
#         "client_status",
#         "SalesRep",
#         "open_popup_button"
#     ]
    
#     list_editable = ['client_status']
    
#     form = CashierOrderForm  # Use the custom form
    
#     def open_popup_button(self, obj):
#         if obj.client.email:
#             return format_html(f"""
# <div class="popup-container">
#     <a href="#" class="openPopup ui-btn ui-corner-all ui-shadow ui-btn-inline">Open Client Data</a>
#     <div class="popup">
#         <div class="popup-content">
#             <iframe name="my_iframe" data-src="{self.get_popup_url(obj)}" class="videoIframe" style="display: none; margin-left: -360%; margin-top: 10%;" width="450%" height="400px" seamless=""></iframe>
#         </div>
#     </div>
# </div>
#             """)
#         else:
#             return "No email available"
    
#     open_popup_button.short_description = 'Open Client Data'
    
#     def get_popup_url(self, obj):
#         # Ensure this method returns the URL string for the iframe
#         return f'/core/user_ordered_items/{obj.client.email}/'
    
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

#     class Media:
#         # css = {
#         #     'all': ("/static/admin/css/admin_button_client.css",)
#         # }
#         js = ("/static/assets/js/vendor/jquery-3.6.0.min.js", '/static/admin/js/open_popup.js')






# from django import forms
# from django.contrib import admin
# from django.utils.html import format_html
# from .models import CashierTable, User  # Import your models
# class CashierOrderForm(forms.ModelForm):
#     class Meta:
#         model = CashierTable
#         fields = '__all__'

#     # Override SalesRep field to show only Sales Representatives
#     SalesRep = forms.ModelChoiceField(
#         queryset=User.objects.filter(client_status='Sales Representative'),
#         label='Sales Representative',
#         widget=forms.Select(attrs={'style': 'width: 200px; color: blue;'})  # Example inline styles
#     )
#     client_status = forms.CharField(
#         widget=forms.TextInput(attrs={'style': 'width: 150px; background-color: lightyellow;'}),  # Example inline style
#     )

# # Custom form widget for selecting SalesRep
# class SalesRepSelectWidget(forms.Select):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Queryset to fetch Sales Representatives
#         print(list(User.objects.filter(client_status='Sales Representative').values_list('id', 'username').values()))
#         self.choices = User.objects.filter(client_status='Sales Representative').values_list('id', 'username')

# # Define your admin class

# CLIENT_ORDER_STATUS = [
#     ("New", "New"),
#     ("In Progress", "In Progress"),
#     ("On Delivery", "On Delivery"),
#     ("Finished", "Finished"),
# ]
# class CasherOrderItemsAdmin(admin.ModelAdmin):
#     search_fields = ['client__username', 'SalesRep__username', 'client_status',"order_number"]
    
#     list_display = [
#         "order_number",
#         "order_date",
#         "client",
#         "address",
#         "client_number",
#         "total_price",
#         "sales_rep",
#         "open_popup_button",  # Custom method for the button
#         "client_status",
#         "client_status_widget"
#     ]
    
#             # "client_status_widget",

#     # list_editable = ['client_status' ]  # Make client_status and SalesRep editable directly in the list view
    
#     form = CashierOrderForm  # Use the custom form
    
#     def sales_rep(self, obj):
#         # Form widget for SalesRep selection
#         form_field = forms.ModelChoiceField(
#             queryset=User.objects.filter(client_status='Sales Representative'),
#             widget=forms.Select(attrs={'style': 'width: 200px; color: blue;'}),
#             initial=obj.SalesRep_id if obj.SalesRep else None,
#         )
#         form = form_field.widget.render(
#             name='SalesRep',
#             value=obj.SalesRep_id if obj.SalesRep else None,
#             attrs={'data-url': '/admin/your_app/user/'},
#         )
#         return form
    
#     sales_rep.short_description = 'Sales Representative'  # Set the column header text
#     def client_status_widget(self, obj):
#         form_field = forms.ChoiceField(
#             choices=CLIENT_ORDER_STATUS,
#             initial=obj.client_status if obj.client_status else None,
#             widget=forms.Select(attrs={'style': 'width: 200px; color: red;'})  # Example class for custom styling
#         )
#         return form_field.widget.render(
#             name='client_status',
#             value=obj.client_status if obj.client_status else None,
#             attrs={}
#         )
#     def open_popup_button(self, obj):
#         if obj.client.email:
#             return format_html(f"""
# <div class="popup-container" style="margin-left:50px;">
#     <a href="#" class="openPopup ui-btn ui-corner-all ui-shadow ui-btn-inline">Open Client Data</a>
#     <div class="popup">
#         <div class="popup-content">
#             <iframe name="my_iframe" data-src="{self.get_popup_url(obj)}" class="videoIframe" style="display: none; margin-left: -480%; margin-top: 15%;" width="550%" height="450px" seamless=""></iframe>
#         </div>
#     </div>
# </div>
#             """)
#         else:
#             return "No email available"
    
#     open_popup_button.short_description = 'Open Client Data'  # Set the column header text
    
#     def get_popup_url(self, obj):
#         # Define logic to return the URL for the popup iframe
#         return f'/core/user_ordered_items/{obj.client.email}'
    
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

#     class Media:
#         # css= {
#         #     'all': ("/static/admin/css/admin_button_client.css",)
#         # }
#         js = ("/static/assets/js/vendor/jquery-3.6.0.min.js", '/static/admin/js/open_popup.js')




















from django.contrib import admin
from django.utils.html import format_html
from django import forms
from .models import CashierTable, User

# Choices for client_status
CLIENT_ORDER_STATUS = [
    ("New", "New"),
    ("In Progress", "In Progress"),
    ("On Delivery", "On Delivery"),
    ("Finished", "Finished"),
]

class CashierOrderForm(forms.ModelForm):
    class Meta:
        model = CashierTable
        fields = '__all__'

    # Override SalesRep field to show only Sales Representatives
    SalesRep = forms.ModelChoiceField(
        queryset=User.objects.filter(client_status='Sales Representative'),
        label='Sales Representative',
        widget=forms.Select(attrs={'style': 'width: 200px; color: blue;'})  # Example inline styles
    )

    # Custom widget function for client_status
    client_status = forms.ChoiceField(
        choices=CLIENT_ORDER_STATUS,
        widget=forms.Select(attrs={'style': 'width: 150px; color: red;'})  # Example class for custom styling
    )

# Define your admin class
class CasherOrderItemsAdmin(admin.ModelAdmin):
    search_fields = ['client__username', 'SalesRep__username', 'client_status', 'order_number']
    
    list_display = [
        "id",
        "order_number",
        "order_date",
        "client",
        "address",
        "client_number",
        "total_price",
        "client_status_widget",  # Directly refer to model fields
        "sales_rep",
        "open_popup_button",  # Custom method for the button
        "save_button",  # Custom method for save button
    ]
    
    # list_editable = ['client_status']  # Make client_status editable directly in the list view
    
    form = CashierOrderForm  # Use the custom form
    def client_status_widget(self, obj):
        form_field = forms.ChoiceField(
            choices=CLIENT_ORDER_STATUS,
            initial=obj.client_status if obj.client_status else None,
            widget=forms.Select(attrs={'style': 'width: 200px; color: red;'})  # Example class for custom styling
        )
        return form_field.widget.render(
            name='client_status',
            value=obj.client_status if obj.client_status else None,
            attrs={}
        )
    def sales_rep(self, obj):
        # Form widget for SalesRep selection
        form_field = forms.ModelChoiceField(
            queryset=User.objects.filter(client_status='Sales Representative'),
            widget=forms.Select(attrs={'style': 'width: 200px; color: blue;'}),
            initial=obj.SalesRep_id if obj.SalesRep else None,
        )
        form = form_field.widget.render(
            name='SalesRep',
            value=obj.SalesRep_id if obj.SalesRep else None,
            attrs={'data-url': '/admin/your_app/user/'},
        )
        return form
    
    sales_rep.short_description = 'Sales Representative'  # Set the column header text
    
    def open_popup_button(self, obj):
        print(self.get_popup_url(obj))


        if obj.client.email:

            return format_html(f"""
<div class="popup-container" style="margin-left:50px; ">
    <a href="#" class="openPopup ui-btn ui-corner-all ui-shadow ui-btn-inline" >Open Client Data</a>
    <div class="popup">
        <div class="popup-content" style=" margin-top: 15%; ">
            <iframe name="my_iframe" data-src="{self.get_popup_url(obj)}" class="videoIframe" style="margin-left:-1000px; display: none;  position: relative; margin-top: 15%; width: 1000px; height: 550px; border: none;" seamless="" ></iframe>
        </div>
    </div>
</div>
            """)
        
        else:
            return "No email available"
        
        
    #             <iframe name="my_iframe" data-src="{self.get_popup_url(obj)}" class="videoIframe" style="display: none; margin-top: 10%; margin-right:auto; left:1px; "  width="100%" height="550px" seamless=""></iframe>

# 
    open_popup_button.short_description = 'Open Client Data'  # Set the column header text
    
    def get_popup_url(self, obj):
        # Define logic to return the URL for the popup iframe
        return f'/core/user_ordered_items/{obj.client.email}/{str(obj.order_number)}'
  
  
  
  
    def save_ajax_data(self, request, object_id):
        if request.method == 'POST' and request.is_ajax():
            # Retrieve the CashierTable instance
            cashier_table_instance = CashierTable.objects.get(pk=object_id)
            
            # Extract data from POST request
            client_status = request.POST.get('client_status')
            sales_rep_id = request.POST.get('SalesRep')
            print(client_status)
            print(sales_rep_id)

            # Update instance fields
            cashier_table_instance.client_status = client_status
            cashier_table_instance.SalesRep_id = sales_rep_id
            
            # Save the updated instance
            cashier_table_instance.save()
            
            # Optionally return a JSON response to confirm success
            return JsonResponse({'success': True})
        








        
        # If method is not POST or not AJAX, return an error response
        return JsonResponse({'error': 'Invalid request'})
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

    def save_button(self, obj):
        return format_html('<input type="submit" class="save-button" value="Save">')

    save_button.short_description = 'Save'  # Set the column header text

    class Media:
        js = ("/static/assets/js/vendor/jquery-3.6.0.min.js", '/static/admin/js/open_popup.js','/static/admin/js/add_new_record_ws.js')  # Include your custom JavaScript file

    def changelist_view(self, request, extra_context=None):
        # Add custom context to include the save button
        if extra_context is None:
            extra_context = {}
        extra_context['show_save_button'] = True
        return super().changelist_view(request, extra_context=extra_context)

# Register the admin class with your model


















































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