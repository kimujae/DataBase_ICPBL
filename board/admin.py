from django.contrib import admin
from .models import Board, Reply, Category, Photo


# Register your models here.
class PhotoInline(admin.TabularInline):
    model = Photo

class BoardAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]


admin.site.register(Board, BoardAdmin)
admin.site.register(Reply)
admin.site.register(Photo)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)