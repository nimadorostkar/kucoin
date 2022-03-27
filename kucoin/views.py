from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from . import models
from .models import Profile
from django.urls import reverse




#------------------------------------------------------------------------------
def index(request):
    img = models.Slider.objects.all()
    item_img = models.ItemImage.objects.all()
    items = models.Item.objects.filter(available=True).order_by("-date")[:11]
    all_items_count = models.Item.objects.filter(available=True).count()
    all_area_count = models.Area.objects.all().count()
    areas = models.Area.objects.all()
    fav = models.Fav.objects.all()
    context = {'img':img,
    'items':items,
    'item_img':item_img,
    'areas':areas,
    'fav':fav,
    'all_items_count':all_items_count,
    'all_area_count':all_area_count}
    return render(request, 'index.html', context)







# End
