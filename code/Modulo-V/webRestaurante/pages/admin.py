from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    ordering        = ('title',)
    search_fields   = ('title', 'content', )
    list_display    = ('title', 'created',)

admin.site.register(Page, PageAdmin)

