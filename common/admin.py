from django.contrib import admin

# Register your models here.
#@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_diplay =(
        'user_id',
        'user_pw',
        'user_name',
        'user_email',
        'user_reg_dt',
       # 'user_house'
    )