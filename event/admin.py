from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    # Display these fields in the event list page
    list_display = ('title', 'category', 'start_time', 'end_time', 'location', 'created_at', 'slug')

    # Allow filtering by category
    list_filter = ('category',)

    # Allow search by title, description, and category
    search_fields = ('title', 'description', 'category__name')

    # Alternatively, you can use fieldsets to group the fields
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'start_time', 'end_time', 'location', 'category', 'image', 'slug')
        }),
    )

    # Allow ordering events by title and category in the admin
    ordering = ('category', 'title')
    
    
    # Optionally, you can add fieldsets for better organization of fields in the form
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'start_time', 'end_time', 'category', 'location', 'image')
        }),
        
    )
    exclude = ['created_at']
# Register the Event model with custom EventAdmin interface
admin.site.register(Event, EventAdmin)

# Customize the Category admin interface
class CategoryAdmin(admin.ModelAdmin):
    # List display for categories in the admin interface
    list_display = ('name', 'description', 'created_at', 'updated_at')  # Adjusted to show description and timestamps

    # Search by category name or description
    search_fields = ('name', 'description')
    
    # Filter categories by the creation date
    list_filter = ('created_at',)

   
    
    # Default ordering by category name
    ordering = ('name',)
    
    

# Register the Category model with custom CategoryAdmin interface
admin.site.register(category, CategoryAdmin)

class ContactAdmin(admin.ModelAdmin):
    # List of fields to display in the admin panel
    list_display = ('name', 'email', 'phone', 'clg_name', 'branch', 'year', 'created_at', 'updated_at')
    
    # Add search functionality by name and email
    search_fields = ('name', 'email')
    
    # Filters by branch and year (if required)
    list_filter = ('branch', 'year')
    
    # Ordering by name and creation date
    ordering = ('name', 'created_at')

# Register the model with the admin site
admin.site.register(Contact, ContactAdmin)