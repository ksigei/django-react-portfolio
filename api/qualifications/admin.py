from django.contrib import admin
from .models import *

# Register your models here.
reg_models = [Education, Experience, Skill, Project, Certification, Award, Language, Interest, Hobby, Reference]

for model in reg_models:
    admin.site.register(model)

    search_fields = ['name', 'description', 'start_date', 'end_date', 'slug', 'institution', 'location', 'qualification', 'field', 'grade', 'start_date', 'end_date', 'slug', 'company', 'location', 
                     'position', 'description', 'start_date', 'end_date', 'slug', 'name', 'proficiency', 'slug', 'name', 'description', 'start_date', 'end_date', 'slug', 'name', 'description' ]
    
    list_display = ['name', 'description', 'start_date', 'end_date', 'slug', 'institution', 'location', 'qualification', 'field', 'grade', 'start_date', 'end_date', 'slug', 'company', 'location',
                    'position', 'description', 'start_date', 'end_date', 'slug', 'name', 'proficiency', 'slug', 'name', 'description', 'start_date', 'end_date', 'slug', 'name', 'description' ]
    
    list_filter = ['name', 'description', 'start_date', 'end_date', 'slug', 'institution', 'location', 'qualification', 'field', 'grade', 'start_date', 'end_date', 'slug', 'company', 'location',
                     'position', 'description', 'start_date', 'end_date', 'slug', 'name', 'proficiency', 'slug', 'name', 'description', 'start_date', 'end_date', 'slug', 'name', 'description' ]
    
    list_per_page = 10
    list_max_show_all = 100

    list_editable = ['name', 'description', 'start_date', 'end_date', 'slug', 'institution', 'location', 'qualification', 'field', 'grade', 'start_date', 'end_date', 'slug', 'company', 'location',
                        'position', 'description', 'start_date', 'end_date', 'slug', 'name', 'proficiency', 'slug', 'name', 'description', 'start_date', 'end_date', 'slug', 'name', 'description' ]
    
    date_hierarchy = 'created_at'
    save_on_top = True
    save_as = True
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = [
        ('Qualification', {'fields': ['name', 'description', 'start_date', 'end_date', 'slug', 'institution', 'location', 'qualification', 'field', 'grade', 'start_date', 'end_date', 'slug', 'company', 'location',
                        'position', 'description', 'start_date', 'end_date', 'slug', 'name', 'proficiency', 'slug', 'name', 'description', 'start_date', 'end_date', 'slug', 'name', 'description' ]}),
        ('Date', {'fields': ['created_at', 'updated_at']}),
    ]

    filter_horizontal = []
    raw_id_fields = []
    autocomplete_fields = []

