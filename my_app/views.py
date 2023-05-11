from django.shortcuts import render
from .models import Student
from .serializer import Studentserializer
from rest_framework import viewsets

# Create your views here.
class studentviewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Studentserializer

# Create your views here.
