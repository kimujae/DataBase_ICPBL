from django.contrib import admin
from .models import Park, Car
# Register your models here.


admin.site.register(Car)
admin.site.register(Park)

class CarAdmin(admin.ModelAdmin):
    list_display =(
        'owner',
        'num',
        'model',
        'entry_time',
        'exit_time',
    )