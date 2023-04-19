from django.contrib import admin
from .models import Order, OrderItem, ShippingAddress

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class ShippingAddressInline(admin.StackedInline):
    model = ShippingAddress
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'status')
    list_filter = ('status',)
    search_fields = ('user__username',)
    inlines = [OrderItemInline, ShippingAddressInline]
    readonly_fields = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('user', 'created_at', 'status')
        }),
    )

admin.site.register(Order, OrderAdmin)
