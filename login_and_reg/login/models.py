from __future__ import unicode_literals
from django.db import models

#create validators here
class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['f_name_short'] = "First name must be at least 2 characters."
        if len(postData['first_name']) > 50:
            errors['f_name_long'] = "First name can't be more than 50 characters."

        if len(postData['last_name']) < 2:
            errors['l_name_short'] = "First name must be at least 2 characters."
        if len(postData['last_name']) > 50:
            errors['l_name_long'] = "First name can't be more than 50 characters."

        if len(postData['email']) == 0:
            errors['long_email'] = "Email Required.
        if len(postData['email']) > 50:
            errors['long_email'] = "Email is too long.  Must be no more than 50 characters."

        if len(postData['password']) < 8:
            errors['email_short'] = "Password must be at least 8 characters."
        if len(postData['password']) > 128:
            errors['email_short'] = "Password must be at least 8 characters."
        return errors 

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()