from django.contrib import admin
from .models import OrderRequest


@admin.register(OrderRequest)
class OrderRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "product_name", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "phone", "message", "product_name")
    readonly_fields = ("created_at",)
