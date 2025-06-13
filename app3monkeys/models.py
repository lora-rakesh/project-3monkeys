from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)   # ✅ file upload
    image_url = models.URLField(blank=True, null=True)                             # ✅ or URL

    price = models.CharField(max_length=100)
    capacity = models.CharField(max_length=100)
    amenities = models.JSONField(default=list)
    contact = models.EmailField()
    phone = models.CharField(max_length=20)
    highlights = models.JSONField(default=list)

    def __str__(self):
        return self.title

    def get_main_image(self):
        return self.image.url if self.image else self.image_url


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image_file = models.ImageField(upload_to='event_images/gallery/', blank=True, null=True)  # ✅ upload
    image_url = models.URLField(blank=True, null=True)                                        # ✅ or URL

    def __str__(self):
        return f"{self.event.title} - Image"

    def get_image(self):
        return self.image_file.url if self.image_file else self.image_url
