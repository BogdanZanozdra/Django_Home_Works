from django.contrib import admin

from .models import Product, Customer, Order


class CustomerAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'registration_date']
    ordering = ['name', 'registration_date']
    list_filter = ['name']
    search_fields = ['name', 'phone_number']
    search_help_text = 'Serch by name and phone_number'
    # fields = ['name', 'email', 'phone_number', 'address', 'registration_date']
    readonly_fields = ['registration_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name']
             }
        ),
        (
            'Contacts',
            {
                'classes': ['collapse'],
                'description': 'Contact information',
                'fields': ['email', 'phone_number', 'address'],
            }
        ),
        (
            'Other information',
            {
                'fields': ['registration_date']
            }
        )
    ]


class ProductAdmin(admin.ModelAdmin):

    @admin.action(description='Reset quantity to 0')
    def reset_quantity(modeladmin, request, queryset):
        queryset.update(count=0)

    list_display = ['product_name', 'count', 'price']
    ordering = ['product_name', 'price', 'count']
    list_filter = ['product_name', 'price', 'order']
    search_fields = ['product_name', 'description']
    search_help_text = 'Search by product_name and description'
    actions = [reset_quantity]

    readonly_fields = ['adding_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['product_name']
             }
        ),
        (
            'Details',
            {
                'fields': ['description', 'price', 'count'],
            }
        ),
        (
            'Other information',
            {
                'fields': ['adding_date']
            }
        )
    ]


class OrderAdmin(admin.ModelAdmin):

    @admin.action(description='Set discount')
    def set_discount(self, request, queryset):
        for object in queryset:
            object.amount -= (object.amount * 10 / 100)
            object.save()

    list_display = ['pk', 'customer', 'amount', 'date_order']
    ordering = ['pk', 'customer', 'amount', 'date_order']
    list_filter = ['customer', 'date_order', 'amount']
    search_fields = ['pk', 'amount']
    search_help_text = 'Search by order id and amount'
    actions = [set_discount]

    readonly_fields = ['date_order', 'amount']
    fieldsets = [
        (
            'Customer',
            {
                'classes': ['wide'],
                'fields': ['customer']
             }
        ),
        (
            'Details',
            {
                'fields': ['amount', 'date_order', 'products'],
            }
        )
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
