from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# LOGIN ENTRY 
class LoginEntry(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

# CONTACT MESSAGE
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

# EVENT
class Event(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    price = models.CharField(max_length=100)
    capacity = models.CharField(max_length=100)
    amenities = models.TextField(blank=True, null=True)
    contact = models.EmailField()
    phone = models.CharField(max_length=20)
    highlights = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_main_image(self):
        return self.image.url if self.image else self.image_url

# EVENT IMAGES 
class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image_file = models.ImageField(upload_to='event_images/gallery/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.event.title} - Image"

    def get_image(self):
        return self.image_file.url if self.image_file else self.image_url

# BOOK NOW
class Booknow(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    num_persons = models.IntegerField()
    special_requests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.full_name}"

# ACTIVITIES 
class Activity(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    
    def __str__(self):
        return self.title

# CUSTOMER REVIEWS 
class CustomerReview(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)  # Range: 1 to 5
    date = models.DateField(auto_now_add=True)
    review = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.rating}"
