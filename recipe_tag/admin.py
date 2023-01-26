from django.contrib import admin
from .models import RecipeTag

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    pass

admin.site.register(RecipeTag, RecipeAdmin)