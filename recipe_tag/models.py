from django.db import models
from tag.models import Tag

# Create your models here.
class RecipeTag(models.Model):
    tag_ID = models.ForeignKey(Tag, on_delete=models.CASCADE)
    recipe_ID = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    createdBy = models.IntegerField(default=None, blank=True, null=True)
    addedAt = models.DateTimeField(auto_now=True)