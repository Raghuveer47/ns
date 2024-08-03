# admin.py
from django.contrib import admin
from .models import Inquiry, AdminDecision

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'people', 'travel_date', 'submitted_at')
    search_fields = ('name', 'phone', 'email')

@admin.register(AdminDecision)
class AdminDecisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'show_modal')  # Make 'id' the first field
    list_editable = ('show_modal',)  # Allow 'show_modal' to be editable
