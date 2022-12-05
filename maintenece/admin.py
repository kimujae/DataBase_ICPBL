from django.contrib import admin
from .models import Maintenence

# Register your models here.
class MaintenenceAdmin(admin.ModelAdmin):
    search_fields = ['main_date']


admin.site.register(Maintenence, MaintenenceAdmin)