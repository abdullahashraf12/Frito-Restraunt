from django.urls import path
from .views import get_csrf_token,signup,login


app_name = "userauths_api"

urlpatterns = [
    path("get_csrf_token", get_csrf_token ,name="get_csrf_token"),

    path("signup", signup ,name="signup"),
    path("login", login ,name="login"),
    # path("logout", views.logout_view ,name="logout"),
    # path("fetch_img", views.fetch_img ,name="fetch_img")
    
]