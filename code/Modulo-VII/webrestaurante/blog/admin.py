from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields  = ('created', 'updated',)

class PostAdmin(admin.ModelAdmin):
    readonly_fields  = ('created', 'updated',)
    # list_display = ('title', 'author', 'published')
    ordering = ('author', 'published')
    search_fields = ('title', 'author__first_name', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__first_name', 'categories__name')
    # list_display = ('title','published', 'name_user', 'post_categories')
    list_display = ('title','published', 'get_nombre', 'post_categories')
    
    
    def name_user(self, obj):
        res = ""
        if obj.author.first_name:
            res += obj.author.first_name
        if obj.author.last_name:
            res += " " + obj.author.last_name
        return res
    name_user.short_description = 'Autor'

    def post_categories(self, obj):
        res = ""
        for c in obj.categories.all().order_by('name'):
            res += c.name + ", "
        res = res[:len(res)-2]
        return res
    post_categories.short_description = 'Categorías'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
