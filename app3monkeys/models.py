from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    price = models.CharField(max_length=100)
    capacity = models.CharField(max_length=100)
    contact = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField()

class EventAmenity(models.Model):
    event = models.ForeignKey(Event, related_name='amenities', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class EventHighlight(models.Model):
    event = models.ForeignKey(Event, related_name='highlights', on_delete=models.CASCADE)
    text = models.TextField()

