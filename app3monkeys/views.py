from django.shortcuts import render
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import AllowAny

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]

