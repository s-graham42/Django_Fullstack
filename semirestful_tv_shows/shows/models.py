from __future__ import unicode_literals
from django.db import models
from datetime import *

# Create your models here.
class ShowManager(models.Manager):
    def new_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title must be at least 2 characters."
        if Show.objects.filter(title=postData['title']):
            errors['duplicate_title'] = "Title must be unique."
        if len(postData['network']) < 3:
            errors['network'] = "Network must be at least 3 characters."
        if len(postData['release_date']) == 0:
            errors['no_release_date'] = "Please enter a Release Date"
        elif datetime.strptime(postData['release_date'], '%Y-%m-%d') > datetime.today():
            errors['release_date'] = "Release Date must be in the past."
        if len(postData['description']) < 10 and len(postData['description']) > 0:
            errors['description'] = "If a Description is entered, it must be at least 10 characters."
        return errors

    def edit_validator(self, postData, show_id):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title must be at least 2 characters."
        if Show.objects.filter(title=postData['title']).exclude(id=show_id):
            errors['duplicate_title'] = "Title must be unique."
        if len(postData['network']) < 3:
            errors['network'] = "Network must be at least 3 characters."
        if len(postData['release_date']) == 0:
            errors['no_release_date'] = "Please enter a Release Date"
        elif datetime.strptime(postData['release_date'], '%Y-%m-%d') > datetime.today():
            errors['release_date'] = "Release Date must be in the past."
        if len(postData['description']) < 10 and len(postData['description']) > 0:
            errors['description'] = "If a Description is entered, it must be at least 10 characters."
        return errors

class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 64)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()