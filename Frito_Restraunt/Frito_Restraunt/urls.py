"""
URL configuration for Frito_Restraunt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings

from django.views.static import serve
from core.consumer import GetCart , GetCashierItems , my_orders
from product.admin import CustomChartsAdmin
# from product.admin import custom_admin_site
urlpatterns = [
path('admin/', admin.site.urls),
re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
path("",include('home.urls', namespace='home')),
path('core/', include('core.urls', namespace='core')),
path('userauths_api/', include('userauths_api.urls', namespace='userauths_api')),

path('userauths/', include('userauths.urls')),
    path('product/', include('product.urls')),  # Include the product app URLs
    path('custom_charts/', CustomChartsAdmin().custom_charts_view, name='custom_charts'),

    # path('custom_admin/', custom_admin_site.urls),  # Custom admin site URL

]

websocket_route = [
    re_path(r"^cart/$", GetCart.as_asgi()),  # Matches "wss://frito-restraunt.com/cart"
    re_path(r"^core/ws/cart/admin/$", GetCashierItems.as_asgi()),  # Matches "wss://frito-restraunt.com/core/ws/cart/admin/"
    re_path(r"^my_orders/orders/$", my_orders.as_asgi())  # Matches "wss://frito-restraunt.com/my_orders/orders/"
]
