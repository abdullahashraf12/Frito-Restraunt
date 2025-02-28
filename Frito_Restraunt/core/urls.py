from django.contrib import admin
from django.urls import include,path
from core.views import (index,product_list,category_list,category_product_list_view,get_product_by_id,get_products_name,AddToCardView,show_card,RemoveFromCardView,wishlist,
                        AddToWishCardView,RemoveFromWishCardView,AddReview,message_socket,offers_product_list_view,add_to_cart,
                        remove_from_Card,checkout,checkout_ajax,user_checked_items,my_orders,place_order,user_ordered_items,save_cashier_table,contact_us)
from .consumer import GetCart,GetCashierItems
from django.urls import re_path
app_name = "core"
urlpatterns = [
path("",include("home.urls", namespace='home')),
path("commentProduct/",AddReview.as_view(),name="commentProduct"),
path('ajax/', checkout_ajax, name='checkout_ajax'),  # URL for the checkout AJAX endpoint

path("wishlist_Add/",AddToWishCardView.as_view(),name="wishlist_Add"),
path('remove_from_wish/', RemoveFromWishCardView.as_view(), name='remove_from_wish'),

path("wishlist/",wishlist,name="wishlist"),

# path('remove_from_card/', RemoveFromCardView.as_view(), name='remove_from_card'),
path('removefromcard/', remove_from_Card, name='remove_from_card'),
path('place_order/', place_order, name='place_order'),
# path('add_to_card/', AddToCardView.as_view(), name='add_to_card'),
path('add-to-cart/', add_to_cart, name='add_to_cart'),
path("show_card/",show_card,name="show_card"),
path("message/",message_socket,name="message"),

path("get_products/<pid>",get_product_by_id,name="get_products"),
path("get_products_name/",get_products_name,name="get_products_name"),
path("products/",product_list,name="product_list"),

path("category/",category_list,name="category_list"),
path("user_checked_items/<user>/",user_checked_items,name="user_checked_items"),

path("category/<cid>/",category_product_list_view,name="category_product_list"),
path("offers/<oid>/",offers_product_list_view,name="offers_product_list_view"),
path('checkout/', checkout,name="checkout"),
path('my_orders/', my_orders,name="my_orders"),
path('user_ordered_items/<user_email>/<int:order_number>/', user_ordered_items,name="user_ordered_items"),
# path('all_useres_ordered/', user_ordered_items,name="user_ordered_items"),

path('save_cashier_table/<int:id>', save_cashier_table, name="save_cashier_table"),
path('contact_us/', contact_us, name="contact_us"),
path('admin/', admin.site.urls),
path("user/",include("userauths.urls")),

]

# websocket_route=[
#     re_path(r'core/ws/cart/$', GetCart.as_asgi()),
#     re_path(r'^core/ws/cart/admin/$', GetCashierItems.as_asgi()),
# ]