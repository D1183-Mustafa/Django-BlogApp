from django.urls import path,include
from .views import home,register,login_request,logout_request
urlpatterns = [
    path("", home,name="home"),
    path("register/", register,name="register"),
    path("login/", login_request,name="login"),
    path("logout/", logout_request,name="logout"),
]