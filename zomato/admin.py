from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Zomato

# Register your models here.
class ZomatoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...
    
admin.site.register(Zomato,ZomatoAdmin)