from django.contrib import admin
from .models import Service, Order

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_display = ('title', 'sub_title', 'updated',)

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_display = ('email', 'name', )

admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)