from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'surveyForm/index.html')

def process_form(request):

    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect ('/result')

def result(request):
    return render(request, 'surveyForm/result.html')
