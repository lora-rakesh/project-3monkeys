from rest_framework import viewsets, permissions
from .models import Event
from .serializers import EventSerializer
from .models import LoginEntry
from .serializers import LoginSerializer
from .models import ContactMessage
from .serializers import ContactMessageSerializer
from .models import Booknow
from .serializers import BooknowSerializer
from .models import Activity
from .serializers import ActivitySerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status

import math

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
from .serializers import RegisterSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # ✅ Required for ModelViewSet
    serializer_class = RegisterSerializer
    http_method_names = ['post']
    permission_classes = [permissions.AllowAny]  # ✅ Allow public access to register


from rest_framework import viewsets
from .models import CustomerReview
from .serializers import CustomerReviewSerializer

class CustomerReviewViewSet(viewsets.ModelViewSet):
    queryset = CustomerReview.objects.all().order_by('-date')
    serializer_class = CustomerReviewSerializer
    http_method_names = ['get', 'post']






