from rest_framework import serializers
from .models import ContactMessage
from .models import Event, EventImage
from .models import LoginEntry
from .models import Booknow

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
