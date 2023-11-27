from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    ordering        = ('title',)
    search_fields   = ('title', 'content', )
    list_display    = ('title', 'subtitle', 'created')

admin.site.register(Service, ServiceAdmin)

