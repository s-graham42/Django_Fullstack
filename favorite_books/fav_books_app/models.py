from __future__ import unicode_literals
from django.db import models
from login.models import User

# create managers here
class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) == 0:
            errors['no_title'] = "A Title is required."
        if len(postData['title']) > 255:
            errors['long_title'] = "Title too long.  Title must be under 255 characters."

        if len(postData['description']) < 5 and len(postData['description']) > 0:
            errors['short_desc'] = "Description too short.  Must be at least 5 characters."
        return errors

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(null=True)
    uploaded_by = models.ForeignKey(User, related_name='books_uploaded', on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name='books_liked')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()