from django.contrib import admin
from . import models
from .models import Exchange





#------------------------------------------------------------------------------
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    list_filter = ('user',)
    search_fields = ('name',)
admin.site.register(Exchange, ExchangeAdmin)















#End
