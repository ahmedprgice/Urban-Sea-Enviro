from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'service_type',
        'date',
        'time',
        'status',
        'created_at'
    )
    list_filter = ('service_type', 'status', 'date')
    search_fields = ('address',)
