from django.contrib import admin
from . import models
from .models import Profile






#------------------------------------------------------------------------------
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'image_tag')
admin.site.register(models.Profile, ProfileAdmin)
