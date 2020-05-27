from django.shortcuts import render
from rest_framework import viewsets
from .models import HumedadAire
from .serializers import HumedadAireSerializer

class HumedadAireViewSet(viewsets.ModelViewSet):
    queryset = HumedadAire.objects.all().order_by('-created')
    serializer_class = HumedadAireSerializer