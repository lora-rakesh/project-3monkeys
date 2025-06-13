from rest_framework import serializers
from .models import ContactMessage, Event, EventImage

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
            'price', 'capacity', 'contact', 'phone', 'images'
        ]

    def get_main_image(self, obj):
        return obj.get_main_image()
