from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
# Create your views here.

def index(request):
    try:
        if request.session["logged_in"] == False:
            return render(request,'Login/login_reg.html')
        else:
            return redirect('/books')
    except:
        request.session["logged_in"] = False
        return render(request, 'Login/login_reg.html')

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

def logout(request):
    request.session['logged_in'] = False
    del request.session['user_alias']
    del request.session['user_email']
    return redirect("/")
