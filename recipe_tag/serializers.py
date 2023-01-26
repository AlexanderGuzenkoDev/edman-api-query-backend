from rest_framework import serializers
from .models import RecipeTag
from tag.models import Tag
from tag.serializers import TagSerializer

class RecipeTagSerializer(serializers.ModelSerializer):
    tag_ID = TagSerializer(read_only=True)
    class Meta:
        model = RecipeTag
        fields = ('id', 'tag_ID', 'recipe_ID', 'createdBy', 'addedAt', 'active')