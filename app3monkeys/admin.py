from django.contrib import admin
from .models import ContactMessage, Event, EventImage, LoginEntry, Booknow, Activity, ActivityDetails, CustomerReview

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')  # fields to show in list view
    search_fields = ('name', 'email', 'message')      # enable search
    list_filter = ('submitted_at',)                   # add filter by date

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):  # ✅ Correct base class
    inlines = [EventImageInline]
    list_display = ('title', 'type', 'date')
admin.site.register(Booknow)
admin.site.register(EventImage)
admin.site.register(ContactMessage)
admin.site.register(LoginEntry)
admin.site.register(Activity)
admin.site.register(CustomerReview)
admin.site.register(ActivityDetails)
