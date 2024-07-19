from django.contrib import admin
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'people', 'travel_date', 'submitted_at')
    search_fields = ('name', 'phone', 'email')
