from django.urls import path, include
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from .views import ContactMessageViewSet

router = DefaultRouter()
router.register(r'contact', ContactMessageViewSet, basename='contact')
=======
from .views import EventViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='events')
>>>>>>> a9ec0e804e460a9669081974ceff850e2b65cd17

urlpatterns = [
    path('api/', include(router.urls)),
]
