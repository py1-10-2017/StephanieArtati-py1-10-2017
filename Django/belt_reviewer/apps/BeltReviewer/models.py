from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime
import bcrypt
from apps.Login.models import *
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$') # regex pattern for email

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name = "books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class ReviewManager(models.Manager):

    def delete_review(self, review_id):
        self.get(id=review_id).delete()
        return self

    def add_review_to_book(self, postData, book_id, user_email):
        book = Book.objects.get(id=book_id)
        user = User.objects.get(email=user_email)
        review = Review.objects.create(rating=int(postData['rating']), review=postData['review'], user=user, book=book)
        return review

    def insert_review(self, postData, email):

        try:
            title = postData['title']
            author_name = postData['author_name']
            author_select = postData['author_select']
        except:
            pass

        if author_name != "":
            author = author_name
        else:
            author = author_select

        review = postData['review']
        rating = int(postData['rating'])

        if len(Author.objects.filter(name=author)) == 0:
            author_object = Author.objects.create(name=author)
        else:
            author_object = Author.objects.get(name=author)

        if len(Book.objects.filter(title=title, author=author_object)) == 0:
            book_object = Book.objects.create(title=title, author=author_object)
        else:
            book_object = Book.objects.get(title=title, author=author_object)

        user_object = User.objects.get(email=email)
        return self.create(review=review, rating=rating, book=book_object, user=user_object)

class Review(models.Model):
    rating = models.IntegerField()
    review = models.TextField()
    user = models.ForeignKey(User, related_name = "reviews")
    book = models.ForeignKey(Book, related_name = "reviews")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = ReviewManager() # this links User class to the User Manager override
