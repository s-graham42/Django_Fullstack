from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

#create validators here
class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['f_name_short'] = "First name must be at least 2 characters."
        if len(postData['first_name']) > 50:
            errors['f_name_long'] = "First name can't be more than 50 characters."
        if not NAME_REGEX.match(postData['first_name']):
            errors['f_name_regex'] = "First Name can only contain letters; no numbers, spaces or special characters."

        if len(postData['last_name']) < 2:
            errors['l_name_short'] = "Last name must be at least 2 characters."
        if len(postData['last_name']) > 50:
            errors['l_name_long'] = "Last name can't be more than 50 characters."
        if not NAME_REGEX.match(postData['last_name']):
            errors['l_name_regex'] = "Last Name can only contain letters; no numbers, spaces or special characters."

        if len(postData['email']) == 0:
            errors['req_email'] = "Email Required."
        if len(postData['email']) > 50:
            errors['long_email'] = "Email is too long.  Must be no more than 50 characters."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_regex'] = "Not a valid email address."

        if len(postData['password']) < 8:
            errors['email_short'] = "Password must be at least 8 characters."
        if len(postData['password']) > 128:
            errors['email_long'] = "Password is too long.  Must be no more than 50 characters."
        if postData['password'] != postData['password_conf']:
            errors['no_pw_match'] = "Password confirmation failed.  Does not match."
        return errors 

    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        login_user = User.objects.filter(email=postData['email'])
        if len(postData['email']) == 0:
            errors['req_email'] = "Email Required."
        if len(postData['email']) > 50:
            errors['long_email'] = "Email is too long.  Must be no more than 50 characters."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_regex'] = "Not a valid email syntax."
        if not login_user:
            errors['not_found'] = "That email does not appear to be in our database."

        if len(postData['password']) < 8:
            errors['email_short'] = "Password must be at least 8 characters."
        if len(postData['password']) > 128:
            errors['email_long'] = "Password is too long.  Must be no more than 50 characters."
        if login_user:
            logged_user = login_user[0]
            if not bcrypt.checkpw(postData['password'].encode(), logged_user.password.encode()):
                errors['bad_pw'] = "Password Authentication Failed"
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