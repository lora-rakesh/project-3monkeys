from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactMessageViewSet, EventViewSet, LoginViewSet, CustomerReviewViewSet, BooknowViewSet, ActivityViewSet, RegisterViewSet
from .views import ActivityDetailsViewSet  # or ActivityDetailsListView


router = DefaultRouter()
router.register(r'contact', ContactMessageViewSet, basename='contact')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'events', EventViewSet, basename='events')
router.register(r'book-now', BooknowViewSet, basename='book-now')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'signup', RegisterViewSet, basename='signup')
router.register(r'reviews', CustomerReviewViewSet, basename='reviews')
router.register(r'activitydetails', ActivityDetailsViewSet, basename='activitydetails')

urlpatterns = [
    path('api/', include(router.urls)),
]
