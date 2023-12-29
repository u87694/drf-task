from django.contrib import admin
from .models import Author, Book

# registering the models for the admin site
admin.site.register(Author)
admin.site.register(Book)