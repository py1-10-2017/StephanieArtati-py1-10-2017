from django.shortcuts import render, redirect, HttpResponse
from .models import User
from validate_email import validate_email
from django.contrib import messages

import re # alternative email validation with regex
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$') # regex pattern for email
# Create your views here.
def index(request):
    users_list = User.objects.all()
    context = {
        "users_list": users_list
    }
    return render(request, 'user_db/users.html', context)

def new(request):
    return render(request, 'user_db/new_user.html')

def create(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']

    errors = User.objects.basic_validator(request.POST)

    if len(errors):
        print(errors)
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/new')
    else:
        User.objects.create(first_name=first_name, last_name=last_name, email_address=email)
        return redirect('/users')

def show_and_update(request, user_id):

    if request.method == 'GET':
        context = {
            "user": User.objects.get(id=user_id)
        }
        return render(request, 'user_db/show_user.html', context)
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        errors = User.objects.basic_validator(request.POST)

        if len(errors):
            print(errors)
            for tag, error in errors.items():
                messages.error(request, error, extra_tags=tag)
            return redirect('/users/'+user_id+'/edit')
        else:
            u = User.objects.get(id=user_id)
            u.first_name = first_name
            u.last_name = last_name
            u.email_address = email
            u.save()
            return redirect('/users')

def edit(request, user_id):
    context = {
        "user": User.objects.get(id=user_id)
    }
    return render(request, 'user_db/edit_user.html', context)

def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect ("/users")
