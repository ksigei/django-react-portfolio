from django.contrib import admin

from .models import *

# Register your models here and add search fields
reg_models = [Contact, Newsletter, About, SocialMedia]

for model in reg_models:
    admin.site.register(model)

    search_fields = ['name', 'email', 'subject', 'content', 'email', 'content', 'title', 'content', 'name', 'link', 'icon']
    list_display = ['name', 'email', 'subject', 'content', 'email', 'content', 'title', 'content', 'name', 'link', 'icon']
    list_filter = ['name', 'email', 'subject', 'content', 'email', 'content', 'title', 'content', 'name', 'link', 'icon']
    list_per_page = 10
    list_max_show_all = 100
    list_editable = ['name', 'email', 'subject', 'content', 'email', 'content', 'title', 'content', 'name', 'link', 'icon']
    date_hierarchy = 'created_at'
    save_on_top = True
    save_as = True
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = [
        ('Contact', {'fields': ['name', 'email', 'subject', 'content', 'email', 'content', 'title', 'content', 'name', 'link', 'icon']}),
        ('Date', {'fields': ['created_at', 'updated_at']}),
    ]
    filter_horizontal = []
    raw_id_fields = []
    autocomplete_fields = []