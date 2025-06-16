from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactMessageViewSet, EventViewSet, LoginViewSet, CustomerReviewViewSet, BooknowViewSet, ActivityViewSet, RegisterViewSet

router = DefaultRouter()
router.register(r'contact', ContactMessageViewSet, basename='contact')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'events', EventViewSet, basename='events')
router.register(r'book-now', BooknowViewSet, basename='book-now')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'reviews', CustomerReviewViewSet, basename='reviews')



urlpatterns = [
    path('api/', include(router.urls)),
]





