from rest_framework import serializers
from .models import ContactMessage, Event, EventImage, LoginEntry, Booknow, Activity, CustomerReview
from django.contrib.auth.models import User
from .models import BookingDetail

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginEntry
        fields = ['email']

class BooknowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booknow
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'message', 'submitted_at']
        read_only_fields = ['id', 'submitted_at']

class EventImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = EventImage
        fields = ['id', 'image_file', 'image_url', 'image']

    def get_image(self, obj):
        return obj.get_image()

class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, read_only=True)
    main_image = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'type', 'subtype', 'date', 'location',
            'description', 'image', 'image_url', 'main_image',
            'price', 'capacity', 'amenities', 'contact', 'phone', 'images', 'highlights'
        ]

    def get_main_image(self, obj):
        return obj.get_main_image()
    
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already in use.")
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user

class CustomerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerReview
        fields = ['id', 'name', 'rating', 'date', 'review']
        read_only_fields = ['date']  # prevent manual override


from .models import Activitydetails, BookingDetail
from django.contrib.auth import get_user_model

User = get_user_model()

class ActivityDetailsSerializer(serializers.Serializer):
    activityId = serializers.IntegerField(write_only=True)
    title = serializers.CharField(read_only=True)
    date = serializers.DateField()
    guests = serializers.IntegerField()
    specialRequests = serializers.CharField()
    userId = serializers.IntegerField(required=False)

    def create(self, validated_data):
        # Extract foreign keys
        activity_id = validated_data.pop('activityId')
        user_id = validated_data.pop('userId', None)

        # Resolve related objects
        activity = Activitydetails.objects.get(id=activity_id)
        user = User.objects.get(id=user_id) if user_id else None

        # Create and return BookingDetail
        return BookingDetail.objects.create(
            activity=activity,
            user=user,
            **validated_data
        )

    def to_representation(self, instance):
        return {
            'activityId': instance.activity.id,
            'title': instance.activity.title,
            'date': instance.date,
            'guests': instance.guests,
            'specialRequests': instance.specialRequests,
            'userId': instance.user.id if instance.user else None
        }

