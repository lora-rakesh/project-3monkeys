from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactMessageViewSet, EventViewSet, EventDetailsViewSet, LoginViewSet, CustomerReviewViewSet, BooknowViewSet, ActivityViewSet, ActivityDetailsViewSet, RegisterViewSet

router = DefaultRouter()
router.register(r'contact', ContactMessageViewSet, basename='contact')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'events', EventViewSet, basename='events')
router.register(r'book-now', BooknowViewSet, basename='book-now')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'signup', RegisterViewSet, basename='signup')
router.register(r'reviews', CustomerReviewViewSet, basename='reviews')
router.register(r'Activitydetails', ActivityDetailsViewSet, basename='activitydetails')
router.register(r'Eventdetails', EventDetailsViewSet, basename='eventdetails')
urlpatterns = [
    path('api/', include(router.urls)),
]
