from django.contrib import admin
from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'uploaded_at')
    search_fields = ('caption',)
    readonly_fields = ('uploaded_at',)
