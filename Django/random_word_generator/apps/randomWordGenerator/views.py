from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    try:
        request.session['counter'] += 1
    except:
        request.session['counter'] = 1

    context = {
        "random_word": get_random_string(length=14),
        "counter": request.session['counter']
    }
    return render(request, 'randomWordGenerator/index.html', context)

def reset(request):
    try:
        del request.session['counter']
    except:
        pass
    return redirect('/')
