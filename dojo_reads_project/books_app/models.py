from __future__ import unicode_literals
from django.db import models
from login.models import User

# create validators here
class AuthorManager(models.Manager):
    def author_validator(self, postData):
        errors = {}
        if len(postData['author']) < 2:
            errors['short_name'] = "Author name too short.  Must be at least 2 characters."
        if len(postData['author']) > 255:
            errors['long_name'] = "Author name too long.  Must be less than 255 characters."
        return errors

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['short_title'] = "Title too short.  Must be at least 2 characters."
        if len(postData['title']) > 255:
            errors['long_title'] = "Title too long.  Must be less than 255 characters."
        return errors

class ReviewManager(models.Manager):
    def review_validator(self, postData):
        errors = {}
        if len(postData['review']) < 2:
            errors['short_review'] = "Review too short.  Must be at least 2 characters."
        if len(postData['review']) > 1000:
            errors['long_review'] = "Review too long.  Must be less than 1000 characters."

        if int(postData['rating']) < 1 or int(postData['rating']) > 5:
            errors['invalid_rating'] = "Rating invalid.  Must be 1 to 5."
        return errors

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()
    # books_written = list of books associated with this Author

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books_written", on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, related_name="books_reviewed", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
    # reviews_of = list of reviews of this book

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    reviewed_by = models.ForeignKey(User, related_name="reviews_made", on_delete=models.CASCADE)
    book_reviewed = models.ForeignKey(Book, related_name="reviews_of", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()