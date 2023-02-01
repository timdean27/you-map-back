from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SpotSerializer
from .models import User, Spot, Comments

# Create your views here.

class SpotView (viewsets.ModelViewSet):
    serializer_class = SpotSerializer
    queryset = Spot.objects.all()