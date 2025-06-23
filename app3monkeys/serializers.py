from rest_framework import serializers
from .models import ContactMessage, Event, EventImage, LoginEntry, Booknow, Activity, ActivityDetails, CustomerReview 
from django.contrib.auth.models import User
# app3monkeys/serializers.py

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


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
            'description','image_url', 'main_image',
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


class ActivityDetailsSerializer(serializers.ModelSerializer):
    activity= serializers.PrimaryKeyRelatedField(queryset=Activity.objects.all())

    class Meta:
        model = ActivityDetails
        fields = '__all__'
