from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import HeroSerializer, UserSerializer
from .models import Hero, UserProfile


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('userName')
    serializer_class = UserSerializer