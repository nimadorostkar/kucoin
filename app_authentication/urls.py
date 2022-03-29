from django.urls import path
from app_authentication import views



urlpatterns = [
    path('', views.index, name='home'),
    path('client', views.client, name='client'),
]
