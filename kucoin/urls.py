from django.urls import path
from kucoin import views



urlpatterns = [
    path('', views.index, name='home'),
    path('client', views.client, name='client'),
]
