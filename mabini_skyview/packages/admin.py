from django.contrib import admin
from .models import Package


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'max_guests', 'is_featured', 'created_at')
    list_filter = ('is_featured',)
    list_editable = ('is_featured',)
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)
