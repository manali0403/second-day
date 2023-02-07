from django.shortcuts import render
from .models import Blog
from .serializer import BlogSerializer
from rest_framework import viewsets

# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()