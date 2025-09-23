from django.contrib import admin
from .models import ContactMessage, Event, Booknow, Activity,CustomerReview

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')  # fields to show in list view
    search_fields = ('name', 'email', 'message')      # enable search
    list_filter = ('submitted_at',)                   # add filter by date


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):  # ✅ Correct base class
    list_display = ('title', 'type', 'date')
admin.site.register(Booknow)
admin.site.register(ContactMessage)

admin.site.register(Activity)
admin.site.register(CustomerReview)

  
