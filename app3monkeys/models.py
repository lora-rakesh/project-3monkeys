from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
User = get_user_model()


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
    image_url = models.ImageField(blank=True, null=True)
    price = models.CharField(max_length=100)
    capacity = models.CharField(max_length=100)
    amenities = models.TextField(blank=True, null=True)
    contact = models.EmailField()
    phone = models.CharField(max_length=20)
    highlights = models.TextField(blank=True, null=True)

    heading = models.CharField(max_length=255, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    passes = models.TextField(blank=True, null=True)
    special_requests = models.TextField(blank=True, null=True)
    schedule = models.TextField(blank=True, null=True)
    performers = models.TextField(blank=True, null=True)
    ticket_includes = models.TextField(blank=True, null=True)
    restrictions = models.TextField(blank=True, null=True)
    safety_guidelines = models.TextField(blank=True, null=True)
    location_map = models.URLField(blank=True, null=True)
    faq = models.TextField(blank=True, null=True)
    images = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title
    def get_main_image(self):
        main_image = self.image.first()  # gets first related EventImage
        return main_image.get_image() if main_image else self.image_url


# ACTIVITIES 
class Activity(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    image_url = models.ImageField(blank=True, null=True)

    heading = models.CharField(max_length=255, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    passes = models.TextField(blank=True, null=True)
    special_requests = models.TextField(blank=True, null=True)
    schedule = models.TextField(blank=True, null=True)
    performers = models.TextField(blank=True, null=True)
    ticket_includes = models.TextField(blank=True, null=True)
    restrictions = models.TextField(blank=True, null=True)
    safety_guidelines = models.TextField(blank=True, null=True)
    location_map = models.URLField(blank=True, null=True)
    faq = models.TextField(blank=True, null=True)
    images = models.ImageField(blank=True, null=True)

    
    def __str__(self):
        return self.title  # ✅ Correct

# BOOK NOW
class Booknow(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    num_persons = models.IntegerField()
    special_requests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="bookings",null=True,blank=True)
    activity = models.ForeignKey("Activity", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Booking by {self.full_name}"




# CUSTOMER REVIEWS 
class CustomerReview(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)  # Range: 1 to 5
    date = models.DateField(auto_now_add=True)
    review = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.rating}"


