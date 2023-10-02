from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_display = ('title', 'usuario', 'published', 'post_categories')
    search_fields = ('title', 'author__first_name', 'categories__name')
    date_hierarchy = 'published'

    def usuario(self, obj):
        if obj.author.last_name:
            return obj.author.first_name + ' ' + obj.author.last_name
        else:
            return obj.author.first_name

    def post_categories(self, obj):
        res = ''
        for category in obj.categories.all().order_by('name'):
            res += category.name + ', '
        return res[:-2]

    post_categories.short_description  = 'Categorías'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
