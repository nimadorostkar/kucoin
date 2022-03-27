from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.urls import reverse






#------------------------------------------------------------------------------
def index(request):
    name='nima'
    context = {'name':name}
    return render(request, 'index.html', context)











# End
