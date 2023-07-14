from django.contrib import admin

from .models import *

# Register your models here and add search fields
reg_models = [Post, Category, Comment, Reply]

for model in reg_models:
    admin.site.register(model)

    search_fields = ['title', 'content', 'name', 'email', 'content']
    list_display = ['title', 'content', 'name', 'email', 'content']
    list_filter = ['title', 'content', 'name', 'email', 'content']
    list_per_page = 10
    list_max_show_all = 100
    list_editable = ['title', 'content', 'name', 'email', 'content']
    date_hierarchy = 'created_at'
    save_on_top = True
    save_as = True
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = [
        ('Post', {'fields': ['title', 'content', 'slug', 'featured_image', 'category', 'tags', 'author', 'status', 'heart']}),
        ('Date', {'fields': ['created_at', 'updated_at']}),
    ]
    filter_horizontal = ['tags']
    raw_id_fields = ['author']
    autocomplete_fields = ['author']

    



