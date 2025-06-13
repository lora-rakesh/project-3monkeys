from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactMessageViewSet, EventViewSet

router = DefaultRouter()
router.register(r'contact', ContactMessageViewSet, basename='contact')
router.register(r'events', EventViewSet, basename='events')

urlpatterns = [
    path('api/', include(router.urls)),
]
