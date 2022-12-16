from django.contrib import admin
from .models import Contact, ContactMe
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    list_filter = ['created_at']


admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactMe)