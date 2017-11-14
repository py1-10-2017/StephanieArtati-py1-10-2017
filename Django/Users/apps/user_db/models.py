from __future__ import unicode_literals
from django.db import models
from validate_email import validate_email

import re # alternative email validation with regex
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$') # regex pattern for email

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors["first_name"] = "First name can't be empty"
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Last name can't be empty"
        # if not re.match(EMAIL_REGEX,postData['email']): #alternative with regex
        if not validate_email(postData['email']):
            errors["email_address"] = "Email address invalid"
        else:
            if len(self.filter(email_address=postData['email'])) >= 1:
                errors["email_address"] = "Email already in use"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager() # this links User class to the User Manager override
