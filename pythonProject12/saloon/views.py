from django.shortcuts import render
from rest_framework import generics
from .models import Men
from .serializers import MenSerializer


# Create your views here.
class MenListView(generics.ListCreateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer


class MenDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
