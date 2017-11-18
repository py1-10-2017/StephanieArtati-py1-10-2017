from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
# Create your views here.

def show_reviews(request):
    recent_reviews = Review.objects.raw("SELECT * FROM beltreviewer_review ORDER BY created_at DESC LIMIT 3")
    exclude_id_list = []
    for review in recent_reviews:
        exclude_id_list.append(review.book.id)
    other_books = Book.objects.exclude(id__in = exclude_id_list)

    context = {
        "recent_reviews": recent_reviews,
        "other_books": other_books
    }
    return render(request, 'BeltReviewer/user_reviews.html', context)

def add_book_review(request):
    authors = Author.objects.all()
    for author in authors:
        print(author.name)
    context = {
        "authors": authors
    }
    return render(request, 'BeltReviewer/add_book_review.html', context)

def add_review_to_book(request, book_id):

    review = Review.objects.add_review_to_book(request.POST, book_id, request.session['user_email'])
    return redirect('/books/{}'.format(book_id))

def delete_review(request, review_id):
    review = Review.objects.get(id=review_id)
    book_id = review.book.id
    if (review.user.email == request.session['user_email']): #revalidate review created by logged-in user
        review = Review.objects.delete_review(review_id)

    return redirect('/books/{}'.format(book_id))

def post_book_review(request):
    review = Review.objects.insert_review(request.POST, request.session["user_email"])
    book_id = review.book.id
    return redirect('books/{}'.format(book_id))

def show_book_reviews(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = book.reviews.all()

    context = {
        "book": book,
        "reviews": reviews
    }
    return render(request, 'BeltReviewer/book_reviews.html', context)

def show_user(request, user_id):
    user = User.objects.get(id=user_id)
    reviews = user.reviews.all()
    books = []
    for review in reviews:
        if review.book not in books:
            books.append(review.book)
    context = {
        "user": user,
        "num_reviews": len(reviews),
        "books": books
    }
    return render(request, "BeltReviewer/user.html", context)
