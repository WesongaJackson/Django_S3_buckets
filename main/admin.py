from django.contrib import admin

from main.models import UploadImage


@admin.register(UploadImage)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['image','created_at']