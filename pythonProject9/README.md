# Django Book Collection API

This project is a simple Django application with a RESTful API to manage a collection of books. The API supports CRUD operations and includes authentication for write operations.

## Requirements

- asgiref==3.8.1
- Django==5.0.6
- djangorestframework==3.15.2
- sqlparse==0.5.0
- Django REST Framework Authtoken

## Project Setup

### 1. Create a new Django project and app
django-admin startproject myproject
cd myproject
django-admin startapp books 

## Install Dependencies
pip install django djangorestframework djangorestframework.authtoken


##  Update settings.py

INSTALLED_APPS = [
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    'books',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
}

## Migrate the Database
python manage.py makemigrations
python manage.py migrate

## Create a Superuser
python manage.py createsuperuser

## Run the Development Server
python manage.py runserver


### Access the API Endpoints
List all books: GET /api/books/
Retrieve a specific book: GET /api/books/<book_id>/
Create a new book: POST /api/books/ (requires authentication)
Update a book: PUT /api/books/<book_id>/ (requires authentication)
Delete a book: DELETE /api/books/<book_id>/ (requires authentication)

### Authentication
Login: http://127.0.0.1:8000/api-auth/login/
Logout: http://127.0.0.1:8000/api-auth/logout/

### Get Token for User
curl -X POST -d "username=<your_username>&password=<your_password>" http://127.0.0.1:8000/api-token-auth/


## Use Token for Authenticated Requests
curl -H "Authorization: Token <your_token>" -X POST -H "Content-Type: application/json" -d '{"title":"Sample Book","author":"Author Name","published_date":"2023-01-01","isbn":"1234567890123"}' http://127.0.0.1:8000/api/books/
