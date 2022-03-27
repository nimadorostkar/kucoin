from django.urls import path
from kucoin import views



urlpatterns = [
    path('', views.index, name='home'),
]
