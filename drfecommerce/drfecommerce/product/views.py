from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets


from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ViewSet):
  """
  A simple viewset for viewing all categories
  """
  
  queryset = Category.objects.all()
  
  def list(self, request):
    serializer = CategorySerializer(self.queryset, many=True)
    
    return Response(serializer.data)