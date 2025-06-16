from django.contrib import admin
from .models import ContactMessage, Event, EventImage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):  # ✅ Correct base class
    inlines = [EventImageInline]
    list_display = ('title', 'type', 'date')