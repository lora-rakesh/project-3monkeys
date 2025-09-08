from rest_framework import viewsets, permissions, status
from .models import Event,ContactMessage, Booknow, Activity, ActivityDetails, CustomerReview
from .serializers import EventSerializer, LoginSerializer, ContactMessageSerializer,ActivityDetailsSerializer, BooknowSerializer, ActivitySerializer, RegisterSerializer, CustomerReviewSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrLimitedAccess
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .permissions import IsAdminOrReadOnly, IsAdminOrReadWrite, IsAdminOrLimitedAccess
from rest_framework_simplejwt.authentication import JWTAuthentication

class ContactMessageViewSet(viewsets.ModelViewSet):
    serializer_class = ContactMessageSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadWrite]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:  # admin can see all messages
            return ContactMessage.objects.all()
        # normal user -> filter by their email
        return ContactMessage.objects.filter(email=user.email)

    def perform_create(self, serializer):
        # auto-fill email from logged-in user (ignore what user sends)
        serializer.save(email=self.request.user.email, name=self.request.user.username)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

   
from django.contrib.auth import get_user_model, authenticate
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import LoginSerializer  # use your existing serializer

User = get_user_model()


class LoginViewSet(viewsets.ViewSet):
    serializer_class = LoginSerializer
    authentication_classes = []   # disable session/auth
    permission_classes = [AllowAny]  # anyone can access

    # POST /api/login/
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # authenticate uses username internally
        user = authenticate(request, username=user_obj.username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Login successful',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                }
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        
class BooknowViewSet(viewsets.ModelViewSet):
    serializer_class = BooknowSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadWrite]


    def get_queryset(self):
        user = self.request.user
        if user.is_staff:  # admin sees all bookings
            return Booknow.objects.all()
        return Booknow.objects.filter(email=user.email)  # normal user -> only their bookings

    def perform_create(self, serializer):
        serializer.save(email=self.request.user.email)  # auto-fill user email

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Required for ModelViewSet
    serializer_class = RegisterSerializer
    permission_classes = permission_classes = [permissions.AllowAny ]  # Allow public access to register
    http_method_names = ['post'] 
     # Only allow POST and GET methods
class CustomerReviewViewSet(viewsets.ModelViewSet):
    queryset = CustomerReview.objects.all().order_by('-date')
    serializer_class = CustomerReviewSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadWrite]
    
class ActivityDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = ActivityDetailsSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadWrite]
 

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:  # admin sees all activities
            return ActivityDetails.objects.all()
        # normal user -> only see their activities
        return ActivityDetails.objects.filter(userId=user.id)

    def perform_create(self, serializer):
        serializer.save(userId=self.request.user.id)  # auto-assign logged-in user ID

