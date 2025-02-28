from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings

from django.views.static import serve
app_name = "home"
from .views import index,login
urlpatterns = [
path('', index,name='home'),
]
