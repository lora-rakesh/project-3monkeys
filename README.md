#  3Monkeys – Booking Platform for Resorts & Holidays

3Monkeys is a full-stack booking platform designed to let customers discover and reserve experiences like resorts, farmhouses, holiday activities, and more. This project is developed with Django REST Framework and PostgreSQL (Render.com), providing a robust backend API layer for a modern frontend (React + Vite).

---

## Features Implemented
-  JWT Authentication (Login / Register)
-  Role-based access (Vendor & Customer)
-  Property Listing and Filtering
-  Availability Calendar for Bookings
-  Booking System with Price Calculation
-  Wishlist Functionality
-  Customer Reviews
-  File/Image Uploads
-  Admin & Vendor Dashboards (customizable)
-  Scalable and API-ready Architecture

### APIs Available
- `Activities API`
- `Login API`
- `Events API`
- `Contact API`
- `Book Now API`
- `Signup API`
- `Reviwes API`

## Project Structure

project3monkeys/
│
├── app3monkeys/
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ ├── urls.py
│
├── project3monkeys/
│ ├── settings.py
│ ├── urls.py
│
├── manage.py
├── requirements.txt
├── README.md 


## ⚙️ Setup Instructions

1. Clone the Repository
```bash
git clone https://github.com/yourusername/3monkeys-backend.git
cd 3monkeys-backend
## Installation and Setup Instructions
2. Create Project Directory
```
mkdir monkeysdata
cd monkeysdata

3. **Set Up a Virtual Environment**
   ```bash
   python -m venv env
   env\Scripts\activate  # On Windows

4. **Install Django**
   ```bash
   pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary python-decouple

5. **Create Django Project and App**
   ```bash
   django-admin startproject project3tmonkeys 
   cd projectmonkeys
   python manage.py startapp app3monkeys

6. **Make changes in settings.py**
   - Add 'app3monkeys', to the INSTALLED_APPS list.
   - Add 'rest_framework', and 'rest_framework_simplejwt', as well.
   - Configure PostgreSQL Database in settings.py

7. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

8. **Final Setup and Run**
   ```bash
   python manage.py createsuperuser  # Create Superuser for admin panel
   python manage.py runserver   # Run the Development Server
   pip freeze > requirements.txt  # Create Requirements File

## API Documentation – 3Monkeys Booking Platform
#This section documents the available API endpoints currently implemented in the backend.
🔐 Authentication APIs
1. Signup API
Endpoint: /api/signup/

Method: POST

Fields:
 -username (string),
 -email (string),
 -password (string),
 -confirm_password (string)

Description: Registers a new user with provided credentials.

2. Login API
Endpoint: /api/login/

Method: POST

Fields:
 -email (string)

Description: Stores the login entry. (JWT token login not implemented here)

3. Contact API
Endpoint: /api/contact/

Methods: POST, GET

Fields (POST):
 -name (string) 
 -email (string)
 -message (text)

Description: Submits a contact message or retrieves all messages (for admin).

4. Events API
Endpoint: /api/events/

Methods: GET, POST, PUT, DELETE

Fields:
 -title
 -type
 -subtype
 -date
 -location
 -description
 -image, 
 -image_url, 
 -price, 
 -capacity, 
 -amenities, 
 -contact, 
 -phone, 
 -highlights

Description: Manage events (create, view, update, delete).

5. Event Images (handled via nested serializer or related endpoint)

6. Activities API
Endpoint: /api/activities/

Methods: GET, POST, PUT, DELETE

Fields:
 -title
 -type
 -category
 -location
 -description
 -price
 -rating
 -image

Description: Add or retrieve details of various activities.

7. Book Now API
Endpoint: /api/book-now/

Method: POST

Fields: 
 -full_name
 -email
 -phone
 -num_persons
 -special_requests

Description: Allows customers to book an activity or event.

8. Customer Review API
Endpoint: /api/reviews/

Methods: GET, POST, PUT, DELETE

Fields:
 -id (auto-generated)
 -name (string) – Name of the reviewer
 -rating (decimal) – Rating out of 5
 -review (text) – Review message
 -created_at (datetime, auto-generated)
 -Description:

POST: Submit a new review

GET: View all reviews

PUT: Update a specific review (if allowed)

DELETE: Delete a review (admin access)

## Deployment Guide

This section outlines the deployment process for the 3MONKEYS backend using Render and PostgreSQL.  

**Requirements**
Python ≥ 3.9
Django ≥ 4.0
PostgreSQL (Cloud DB or Render-managed)
Render Account (https://render.com)
GitHub Repository (Code must be pushed here)

**Deployment Setup**
 - Push Code to GitHub
 - Ensure backend project is versioned and pushed to a public or private GitHub repository.
 - Go to Render → Dashboard
 - Create a PostgreSQL database
 - Note down:
   DB Name, User, Password, Host, Port
 - Configure Django Settings
   In settings.py update Database details
   ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']  # Hosts allowed to access the app (Render & local)
 - DEBUG = False
 - Set Up Static & Media Files (Optional but recommended for production)

**Deploy on Render**
 - Create a New Web Service
 - Select: "New Web Service"
 - Choose the GitHub repo
 - Environment: Python 3
 - Build Command: pip install -r requirements.txt
 - Start Command: gunicorn projectmonkeys.wsgi:application
 - Add Environment Variables from .env
 - Then Deploy

**Post Deployment**
Test all major API endpoints ( /api/login/, /api/contact/, /api/events/, /api/book-now/ etc.)

