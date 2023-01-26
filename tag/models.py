from django.db import models

# Create your models here.

class Tag(models.Model):
    label = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    createdBy = models.IntegerField(null=True, default=None)
    addedAt = models.DateTimeField(auto_now=True)