from rest_framework import viewsets, permissions, status
from .models import Event, LoginEntry, ContactMessage, Booknow, Activity, CustomerReview, ActivityDetails
from .serializers import EventSerializer, LoginSerializer, ContactMessageSerializer, ActivityDetailsSerializer, BooknowSerializer, ActivitySerializer, RegisterSerializer, CustomerReviewSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    http_method_names = ['post', 'get']

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


User = get_user_model()

class LoginViewSet(viewsets.GenericViewSet):
    serializer_class = LoginSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try:
                user = User.objects.get(email=email)
                if check_password(password, user.password):
                    return Response({'message': 'Login successful'})
                else:
                    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BooknowViewSet(viewsets.ModelViewSet):
    queryset = Booknow.objects.all()
    serializer_class = BooknowSerializer
    http_method_names = ['post','get']  

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Required for ModelViewSet
    serializer_class = RegisterSerializer
    http_method_names = ['post']
    permission_classes = [permissions.AllowAny]  # Allow public access to register

class CustomerReviewViewSet(viewsets.ModelViewSet):
    queryset = CustomerReview.objects.all().order_by('-date')
    serializer_class = CustomerReviewSerializer
    http_method_names = ['get', 'post']


class ActivityDetailsViewSet(viewsets.ModelViewSet):
    queryset = ActivityDetails.objects.all()
    serializer_class = ActivityDetailsSerializer


