from rest_framework import serializers
from .models import ContactMessage, Event,UserDetails, Booknow, Activity,CustomerReview 
from django.contrib.auth.models import User
# app3monkeys/serializers.py

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


from rest_framework import serializers
from .models import Booknow

class BooknowSerializer(serializers.ModelSerializer):
    selected_id = serializers.SerializerMethodField()
    selected_name = serializers.SerializerMethodField()

    class Meta:
        model = Booknow
        fields = [
            'id', 'full_name', 'email', 'phone', 'num_persons', 'special_requests', 'created_at',
            'event', 'activity', 'selected_id', 'selected_name'
        ]

    def get_selected_id(self, obj):
        if obj.event:
            return obj.event.id
        if obj.activity:
            return obj.activity.id
        return None

    def get_selected_name(self, obj):
        if obj.event:
            return obj.event.title  # or name field for Event
        if obj.activity:
            return obj.activity.title
        return None



class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'message', 'submitted_at']
        read_only_fields = ['id', 'submitted_at']



class EventDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = [
            "heading", "info", "passes", "special_requests",
            "schedule", "performers", "ticket_includes",
            "restrictions", "safety_guidelines",
            "location_map", "faq",
        ]
class EventSerializer(serializers.ModelSerializer):
    more_details = EventDetailsSerializer(source="*", required=False)

    class Meta:
        model = Event
        fields = [
            "id", "title", "type", "subtype", "date", "location",
            "description", "image_url",
            "price", "capacity", "amenities", "contact", "phone",
            "highlights",
            "more_details",
        ]

class ActivityDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            "heading", "info", "passes", "special_requests",
            "schedule", "performers", "ticket_includes",
            "restrictions", "safety_guidelines",
            "location_map", "faq",
        ]
class ActivitySerializer(serializers.ModelSerializer):
    more_details = ActivityDetailsSerializer(source="*", required=False)
    class Meta:
        model = Activity
        fields = ["id", "title","category","location","description","price","rating","image_url","more_details",]

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
class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['name', 'email', 'phone', 'address', 'profile_picture']


