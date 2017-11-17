from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
# Create your views here.

def index(request):
    try:
        if request.session["logged_in"] == False:
            return render(request,'BeltReviewer/login_reg.html')
        else:
            return redirect('/books')
    except:
        request.session["logged_in"] = False
        return render(request, 'BeltReviewer/login_reg.html')

def process_registration(request):
    request.session['login'] = False
    request.session['registration'] = True
    errors = User.objects.validate_registration(request.POST)
    if len(errors) == 0:
        request.session['logged_in'] = True
        request.session['user_alias'] = request.POST['alias']
        request.session['user_email'] = request.POST['email']
        return redirect("/books")
    else:
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect("/")

def process_login(request):
    request.session['registration'] = False
    request.session['login'] = True
    email = request.POST['email']
    password = request.POST['password']
    if len(email) < 1:
        messages.error(request, "Email must be specified", extra_tags="invalid email address")
        return redirect('/')
    else:
        if len(User.objects.filter(email=email)) < 1:
            messages.error(request, "No account with specified email address", extra_tags="unknown email address")
            return redirect('/')
        else:
            user = User.objects.get(email=email)
            password_hash = user.password
            if not bcrypt.checkpw(password.encode(), password_hash.encode()):
                messages.error(request, "Invalid password", extra_tags="invalid password")
                return redirect('/')
            else:
                request.session['logged_in'] = True
                request.session['user_alias'] = user.alias
                request.session['user_email'] = user.email
                return redirect('/books')

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

    book = Book.objects.get(id=book_id)
    user = User.objects.get(email=request.session['user_email'])
    Review.objects.create(rating=int(request.POST['rating']), review=request.POST['review'], user=user, book=book)
    return redirect('/books/{}'.format(book_id))

def delete_review(request, review_id):
    review = Review.objects.get(id=review_id)
    book_id = review.book.id
    if (review.user.email == request.session['user_email']): #revalidate review created by logged-in user
        review.delete()

    return redirect('/books/{}'.format(book_id))

def post_book_review(request):
    title = request.POST['title']
    author_name = request.POST['author_name']
    author_select = request.POST['author_select']

    if author_name != "":
        author = author_name
    else:
        author = author_select

    review = request.POST['review']
    rating = int(request.POST['rating'])

    if len(Author.objects.filter(name=author)) == 0:
        author_object = Author.objects.create(name=author)
    else:
        author_object = Author.objects.get(name=author)

    if len(Book.objects.filter(title=title, author=author_object)) == 0:
        book_object = Book.objects.create(title=title, author=author_object)
    else:
        book_object = Book.objects.get(title=title, author=author_object)

    user_object = User.objects.get(email=request.session['user_email'])
    Review.objects.create(review=review, rating=rating, book=book_object, user=user_object  )
    return redirect('books/{}'.format(book_object.id))

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

def logout(request):
    request.session['logged_in'] = False
    del request.session['user_alias']
    del request.session['user_email']
    return redirect("/")
