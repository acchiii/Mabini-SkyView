from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'guests', 'package', 'status', 'created_at')
    list_filter = ('status', 'date', 'created_at')
    search_fields = ('name', 'email', 'package')
    list_editable = ('status',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
