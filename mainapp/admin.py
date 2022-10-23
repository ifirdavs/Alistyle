from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin

# Register your models here.

admin.site.register(Section)

@admin.register(Inner)
class InnerAdmin(ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

admin.site.register(MainSection)
admin.site.register(Product)
admin.site.register(Image)