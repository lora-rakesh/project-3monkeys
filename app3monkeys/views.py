from rest_framework import viewsets, permissions, status
from .models import Event, LoginEntry, ContactMessage, Booknow, Activity, ActivityDetails, CustomerReview
from .serializers import EventSerializer, LoginSerializer, ContactMessageSerializer,ActivityDetailsSerializer, BooknowSerializer, ActivitySerializer, RegisterSerializer, CustomerReviewSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrLimitedAccess

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    http_method_names = ['post', 'get']

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsAdminOrLimitedAccess]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:  # or user.role == "admin"
            return Event.objects.all()  # admin sees all events
        else:
            return Event.objects.filter(created_by=user)  # user sees only their events


from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from .serializers import LoginSerializer
User = get_user_model()
class LoginViewSet(viewsets.GenericViewSet):
    serializer_class = LoginSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if not check_password(password, user.password):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # ✅ generate JWT tokens
        refresh = RefreshToken.for_user(user)
        return Response({
            'message': 'Login successful',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })




class BooknowViewSet(viewsets.ModelViewSet):
    queryset = Booknow.objects.all()
    serializer_class = BooknowSerializer
    permission_classes = [IsAuthenticated, IsAdminOrLimitedAccess]

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated, IsAdminOrLimitedAccess]
class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Required for ModelViewSet
    serializer_class = RegisterSerializer
    http_method_names = ['post']
    permission_classes = [IsAuthenticated, IsAdminOrLimitedAccess]  # Allow public access to register

class CustomerReviewViewSet(viewsets.ModelViewSet):
    queryset = CustomerReview.objects.all().order_by('-date')
    serializer_class = CustomerReviewSerializer
    permission_classes = [IsAuthenticated, IsAdminOrLimitedAccess]

class ActivityDetailsViewSet(viewsets.ModelViewSet):
    queryset = ActivityDetails.objects.all()
    serializer_class = ActivityDetailsSerializer
    permission_classes = [IsAuthenticated, IsAdminOrLimitedAccess]

