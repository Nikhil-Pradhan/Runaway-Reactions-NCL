from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.welcome, name='welcome'),
    path('login', views.login, name='login')
]
