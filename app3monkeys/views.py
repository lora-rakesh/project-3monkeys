from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer

<<<<<<< HEAD
# Create your views here.
from rest_framework import viewsets
from .models import ContactMessage
from .serializers import ContactMessageSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    http_method_names = ['post', 'get']  # allow 'get' too for admin debugging


=======
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
>>>>>>> a9ec0e804e460a9669081974ceff850e2b65cd17
