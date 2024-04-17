from django.contrib import admin
from .models import ClientPrivatPerson, ClientLegalPerson


@admin.register(ClientPrivatPerson)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "address", "created_at", "updated_at")
    search_fields = ("name", "email", "phone", "address", "created_at", "updated_at")
    list_filter = ("name", "email", "phone", "address", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(ClientLegalPerson)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "address", "created_at", "updated_at", "slug")
    search_fields = ("name", "email", "phone", "address", "created_at", "updated_at")
    list_filter = ("name", "email", "phone", "address", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("name", "ICO")}