from rest_framework import serializers
from .models import Event, EventImage, EventAmenity, EventHighlight

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ['id', 'image_url']

class EventAmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAmenity
        fields = ['id', 'name']

class EventHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventHighlight
        fields = ['id', 'text']

class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, read_only=True)
    amenities = EventAmenitySerializer(many=True, read_only=True)
    highlights = EventHighlightSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'type', 'subtype', 'date', 'location',
            'description', 'price', 'capacity', 'contact', 'phone',
            'images', 'amenities', 'highlights'
        ]
