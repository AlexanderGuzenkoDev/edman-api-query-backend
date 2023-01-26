from django.forms import ModelForm
from .models import RecipeTag

class RecipeTagForm(ModelForm):
    class Meta:
        model = RecipeTag
        fields = ['tag_ID', 'recipe_ID']