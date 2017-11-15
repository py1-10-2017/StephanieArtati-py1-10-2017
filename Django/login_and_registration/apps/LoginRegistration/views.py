from django.shortcuts import render, redirect, HttpResponse
from datetime import date, datetime
import bcrypt
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'LoginRegistration/index.html')

def success(request):
    return render(request, 'LoginRegistration/success.html')

def process_registration(request):

    errors = User.objects.validate_registration(request.POST)
    request.session["registration"] = True
    request.session["login"] = False
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        request.session['first_name'] = first_name
        return redirect('/success')

def process_login(request):

    request.session["registration"] = False
    request.session["login"] = True
    email_address = request.POST['email_address']
    password = request.POST['password']
    if len(email_address) < 1:
        messages.error(request, "Email must be specified", extra_tags="invalid email address")
        return redirect('/')
    else:
        if len(User.objects.filter(email_address=email_address)) < 1:
            messages.error(request, "No account with specified email address", extra_tags="unknown email address")
            return redirect('/')
        else:
            user = User.objects.get(email_address=email_address)
            password_hash = user.password
            if not bcrypt.checkpw(password.encode(), password_hash.encode()):
                messages.error(request, "Invalid password", extra_tags="invalid password")
                return redirect('/')
            else:
                request.session['logged_in'] = True
                request.session['first_name'] = user.first_name
                return redirect('/success')

def reset(request):

    del request.session['logged_in']
    del request.session['first_name']
    del request.session['registration']
    del request.session['login']
