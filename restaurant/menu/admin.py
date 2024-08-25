from django.contrib import admin
from .models import Category, MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_category_name', 'price', 'available')
    list_filter = ('category', 'available')  
    search_fields = ('name',)

    def get_category_name(self, obj):
        return obj.category.name
    get_category_name.admin_order_field = 'category'  # Allows sorting by category
    get_category_name.short_description = 'Category'  # Renames the column header

admin.site.register(Category)
admin.site.register(MenuItem, MenuItemAdmin)
