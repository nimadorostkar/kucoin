from django.urls import path
from app_kucoin import views



urlpatterns = [
    path('', views.index, name='home'),
    path('client', views.client, name='client'),
    path('dashboard', views.dashboard, name='dashboard'),
]
