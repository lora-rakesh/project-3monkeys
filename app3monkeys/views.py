from rest_framework import viewsets, permissions, status
from .models import Event, LoginEntry, ContactMessage, Booknow, Activity, CustomerReview
from .serializers import EventSerializer, LoginSerializer, ContactMessageSerializer, BooknowSerializer, ActivitySerializer, RegisterSerializer, CustomerReviewSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    http_method_names = ['post', 'get']

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset = LoginEntry.objects.all()
    serializer_class = LoginSerializer
    http_method_names = ['post','get']

class BooknowViewSet(viewsets.ModelViewSet):
    queryset = Booknow.objects.all()
    serializer_class = BooknowSerializer
    http_method_names = ['post','get']  

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Required for ModelViewSet
    serializer_class = RegisterSerializer
    http_method_names = ['post']
    permission_classes = [permissions.AllowAny]  # Allow public access to register

class CustomerReviewViewSet(viewsets.ModelViewSet):
    queryset = CustomerReview.objects.all().order_by('-date')
    serializer_class = CustomerReviewSerializer
    http_method_names = ['get', 'post']






