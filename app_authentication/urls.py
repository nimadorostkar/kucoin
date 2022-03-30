from django.urls import path
from app_authentication import views



urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]
