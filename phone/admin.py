from django.contrib import admin
from .models import Phone


admin.site.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("phone", "type", "owner_privat", "owner_legal", "created_at", "updated_at", "old_number")
    search_fields = ("phone", "type", "owner_privat", "owner_legal", "created_at", "updated_at", "old_number")
    list_filter = ("phone", "type", "owner_privat", "owner_legal", "created_at", "updated_at", "old_number")

# Register your models here.
