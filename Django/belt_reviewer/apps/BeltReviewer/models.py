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
        if len(postData['name']) < 1:
            errors["name"] = "Name can't be empty"
        if len(postData['alias']) < 1:
            errors["alias"] = "Alias can't be empty"
        if len(postData['email']) < 1:
            errors["email"] = "Email can't be empty"
        else:
            if not re.match(EMAIL_REGEX,postData['email']): #alternative with regex
                errors["email"] = "Email address invalid"
            else:
                if len(self.filter(email=postData['email'])) >= 1:
                    errors["email"] = "Email already in use"
        if len(postData['password']) < 8:
            errors["password"] = "Password can't be fewer than 8 characters"
        else:
            if postData['password'] != postData['password_confirm']:
                errors["password"] = "Password confirmation does not match password"

        if len(errors) == 0: #insert into DB
            name = postData['name']
            alias = postData['alias']
            email = postData['email']
            password_raw = postData['password']
            password_hash = bcrypt.hashpw(password_raw.encode(), bcrypt.gensalt())

            User.objects.create(name=name, alias=alias, email=email, password=password_hash)

        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager() # this links User class to the User Manager override

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name = "books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Review(models.Model):
    rating = models.IntegerField()
    review = models.TextField()
    user = models.ForeignKey(User, related_name = "reviews")
    book = models.ForeignKey(Book, related_name = "reviews")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
