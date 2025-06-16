from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactMessageViewSet, EventViewSet, LoginViewSet
from .views import BooknowViewSet

router = DefaultRouter()
router.register(r'contact', ContactMessageViewSet, basename='contact')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'events', EventViewSet, basename='events')
router.register(r'book-now', BooknowViewSet, basename='book-now')

urlpatterns = [
    path('api/', include(router.urls)),
]

