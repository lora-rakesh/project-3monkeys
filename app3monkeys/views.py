from rest_framework import viewsets
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
    http_method_names = ['post','get']  # Only allow POST (book now)
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer