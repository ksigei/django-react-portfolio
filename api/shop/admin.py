from django.contrib import admin

from .models import *

# Register your models here and add search fields
reg_models = [Product, Cart, CartItem, Order, OrderItem, Search, Review]

for model in reg_models:
    admin.site.register(model)

    search_fields = ['name', 'description', 'price', 'image', 'slug', 'product', 'quantity', 'price', 'order', 'search', 'product']
    list_display = ['name', 'description', 'price', 'image', 'slug', 'product', 'quantity', 'price', 'order', 'search', 'product']
    list_filter = ['name', 'description', 'price', 'image', 'slug', 'product', 'quantity', 'price', 'order', 'search', 'product']
    list_per_page = 10
    list_max_show_all = 100
    list_editable = ['name', 'description', 'price', 'image', 'slug', 'product', 'quantity', 'price', 'order', 'search', 'product']
    date_hierarchy = 'created_at'
    save_on_top = True
    save_as = True
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = [
        ('Product', {'fields': ['name', 'description', 'price', 'image', 'slug', 'product', 'quantity', 'price', 'order', 'search', 'product']}),
        ('Date', {'fields': ['created_at', 'updated_at']}),
    ]
    filter_horizontal = []
    raw_id_fields = []
    autocomplete_fields = []
