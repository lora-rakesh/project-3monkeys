from django.urls import path, include
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from .views import ContactMessageViewSet, EventViewSet

router = DefaultRouter()
router.register(r'contact', ContactMessageViewSet, basename='contact')
=======
from .views import ContactMessageViewSet,EventViewSet

router = DefaultRouter()
router.register(r'contact', ContactMessageViewSet, basename='contact')

>>>>>>> 528cd83f18347f2f073220571866ca1045d87ce1
router.register(r'events', EventViewSet, basename='events')

urlpatterns = [
    path('api/', include(router.urls)),
]
