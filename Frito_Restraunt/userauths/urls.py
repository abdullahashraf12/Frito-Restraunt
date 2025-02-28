from django.urls import path
from userauths import views


app_name = "userauths"

urlpatterns = [
    path("register", views.register_or_login_user ,name="register"),
    path("login", views.register_or_login_user ,name="login"),
    path("logout", views.logout_view ,name="logout"),
    path("fetch_img", views.fetch_img ,name="fetch_img")
    
]