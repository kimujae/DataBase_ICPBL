from django.contrib import admin
from .models import Board, Reply, Category


# Register your models here.
admin.site.register(Board)
admin.site.register(Reply)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)