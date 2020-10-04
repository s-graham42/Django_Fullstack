from __future__ import unicode_literals
from django.db import models

# create validators here.
class CourseManager(models.Manager):
    def course_validator(self, postData):
        errors = {}
        if len(postData['course_name']) < 6 or len(postData['course_name']) > 255:
            errors['short_name'] = "Course Name must be more than 5 characters and less than 255 characters in length."
        if len(postData['description']) < 16:
            errors['short_desc'] = "Description must be more than 15 characters in length."
        return errors

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # description = access description
    objects = CourseManager()
    
class Description(models.Model):
    desc = models.TextField()
    course = models.OneToOneField(Course, related_name="description", on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)