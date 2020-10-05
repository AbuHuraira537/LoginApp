from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name='signup'),
    path('signup1', views.signup1, name='signup1'),
    path('index', views.index, name="index"),
    path('login', views.login, name="login"),
    path('logout',views.login,name="logout"),
    path('loginresult',views.loginresult,name="loginresult")


]