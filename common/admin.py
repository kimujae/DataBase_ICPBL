from django.contrib import admin
from .models import User,UserProfile

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_diplay =(
        'user_id',
        'user_pw',
        'user_first_name',
        'user_last_name',
        'user_reg_dt',
        'user_house'
    )

admin.site.register(UserProfile)