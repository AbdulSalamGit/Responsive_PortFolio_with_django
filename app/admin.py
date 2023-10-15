from django.contrib import admin
from .models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("sender_name", "sender_email", "subject")
    search_fields = ("sender_name", "sender_email", "subject")
    list_filter = ("subject",)
    ordering = ("-id",)


admin.site.register(ContactMessage, ContactMessageAdmin)
