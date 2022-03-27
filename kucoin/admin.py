from django.contrib import admin
from . import models





#------------------------------------------------------------------------------
class ProfileAdmin(ImportExportModelAdmin):
    list_display = ('image_tag', 'user_type', 'user_name','phone','sales_expert')
    list_filter = ('user_type', "date_created")
    search_fields = ['user_name', 'phone']
admin.site.register(models.Profile, ProfileAdmin)














#End
