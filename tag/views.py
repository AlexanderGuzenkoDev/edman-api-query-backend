from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from .serializers import TagSerializer
from .models import Tag
from recipe_tag.models import RecipeTag
from rest_framework.response import Response

# Create your views here.

@api_view(['GET', 'POST'])
@authentication_classes([])
def tags(request):
    # get all custom tags
    # returns:
    #   JSON of all custom tags
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
    # create a custom tag
    # returns:
    #   JSON of a added tag or HTTP error
    elif request.method == 'POST':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([])
# enable or disable a custom tag
# params:
#   pk (number): id of tag stored in the database table
# returns:
#   JSON of updated tag or HTTP error
def set_action(request, pk):
    if request.method == 'PUT':
        tag = get_object_or_404(Tag, pk=pk)
        tagData = {"active": not tag.active}
        tagSerializer = TagSerializer(tag, data=tagData, partial=True)
        
        if tagSerializer.is_valid():
            tagSerializer.save()
            return Response(tagSerializer.data)
        
        return Response(tagSerializer.errors, status=status.HTTP_400_BAD_REQUEST)