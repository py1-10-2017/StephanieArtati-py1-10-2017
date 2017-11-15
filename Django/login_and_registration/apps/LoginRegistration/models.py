from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime
import bcrypt

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$') # regex pattern for email

# Create your models here.
class UserManager(models.Manager):
    def validate_registration(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name can't be fewer than 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name can't be fewer than 2 characters"
        if len(postData['email_address']) < 1:
            errors["email_address"] = "Email must be specified"
        else:
            if not re.match(EMAIL_REGEX,postData['email_address']): #alternative with regex
                errors["email_address"] = "Email address invalid"
            else:
                if len(self.filter(email_address=postData['email_address'])) >= 1:
                    errors["email_address"] = "Email already in use"
        if len(postData['password']) < 8:
            errors["password"] = "Password can't be fewer than 8 characters"
        else:
            if postData['password'] != postData['password_confirm']:
                errors["password"] = "Password confirmation does not match password"
        try:
            birthdate_str = postData['birthdate']
            birthdate_yyyymmdd = birthdate_str.split('-')
            birthdate = date(int(birthdate_yyyymmdd[0]), int(birthdate_yyyymmdd[1]), int(birthdate_yyyymmdd[2]))
            today = date.today()
            if (today-birthdate).days < 0:
                errors['birthday'] = "Birthday must be prior to today"
        except:
            errors['birthday'] = "Invalid or unspecified birthdate"

        if len(errors) == 0: #insert into DB
            first_name = postData['first_name']
            last_name = postData['last_name']
            email_address = postData['email_address']

            password_raw = postData['password']
            password_hash = bcrypt.hashpw(password_raw.encode(), bcrypt.gensalt())

            birthdate_str = postData['birthdate']
            birthdate_yyyymmdd = birthdate_str.split('-')
            birthdate = date(int(birthdate_yyyymmdd[0]), int(birthdate_yyyymmdd[1]), int(birthdate_yyyymmdd[2]))
            birthdatetime = datetime.combine(birthdate, datetime.min.time())

            User.objects.create(first_name=first_name, last_name=last_name, email_address=email_address, birthdate=birthdatetime, password=password_hash)

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthdate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager() # this links User class to the User Manager override
