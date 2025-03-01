from django.contrib import admin
from .models import Category, Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_categories')
    search_fields = ('title', 'ingredients')

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories.short_description = 'Categories'


admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)