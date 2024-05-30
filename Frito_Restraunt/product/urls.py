from django.urls import path
from .views import print_posted_categ_and_textfield

app_name = "product"

urlpatterns = [
    path('search/', print_posted_categ_and_textfield, name='search'),
]
