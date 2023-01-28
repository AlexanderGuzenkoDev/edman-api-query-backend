from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from .serializers import RecipeTagSerializer
from .models import RecipeTag
from tag.models import Tag
from rest_framework.response import Response
from django.core import serializers
from .forms import RecipeTagForm
import json

# Create your views here.

@api_view(['GET', 'POST'])
@authentication_classes([])
def recipeTags(request):
    # get all recipe tags
    # returns: 
    #   JSON of all recipe tags
    if request.method == 'GET':
        recipeTags = RecipeTag.objects.all()
        serializer = RecipeTagSerializer(recipeTags, many=True)
        return Response(serializer.data)
    
    # add a tag to a recipe
    # returns:
    #   JSON of a added tag or HTTP error
    elif request.method == 'POST':
        form = RecipeTagForm(request.data)

        if form.is_valid():
            recipeTag = RecipeTag(
                tag_ID=form.cleaned_data['tag_ID'],
                recipe_ID=form.cleaned_data['recipe_ID']
            )
            
            recipeTag.save()
            
            serializer = RecipeTagSerializer(recipeTag)
            return Response(serializer.data)
        else:
            return Response(form.errors.as_json(), status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([])
# delete a tag from a recipe
# params:
#   pk (number): id of recipe tag stored in the database table
# returns:
#   string: Deleted Successfully
def set_action(request, pk):
    if request.method == 'DELETE':
        recipeTag = get_object_or_404(RecipeTag, pk=pk)
        print(recipeTag.delete())
        
        return Response('Deleted Successfully')