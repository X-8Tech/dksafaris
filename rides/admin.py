from django.contrib import admin
from .models import RideRequest

@admin.register(RideRequest)
class RideRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'pickup', 'destination', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'phone', 'pickup', 'destination')
    ordering = ('-created_at',)
