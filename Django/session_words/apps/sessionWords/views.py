from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime

# Create your views here.
def index(request):
    return render(request, "sessionWords/index.html")

def process_form(request):
    if 'words_list' not in request.session:
        request.session['words_list'] = []
    if 'counter' not in request.session:
        request.session['counter'] = 0
    # words_list session update doesn't work without codeline below
    request.session['counter'] += 1

    new_word = request.POST['word']
    color = request.POST['color']
    t_str = strftime("%r, %B %d, %Y",gmtime())

    if 'font_size' in request.POST:
        big_font_size = True
        # request.session['words_list'].append("<p><span class='"+color+" "+"big'>"+new_word+"</span> --- added on "+t_str+"</p>")
    else:
        # request.session['words_list'].append("<p><span class='"+color+"'>"+new_word+"</span> --- added on "+t_str+"</p>")
        big_font_size = False
    new_word_dict = {
        "word": new_word,
        "color": color,
        "time": t_str,
        "big_font": big_font_size
    }
    request.session['words_list'].append(new_word_dict)
    print(request.session['words_list'])
    return redirect('/')

def reset(request):
    try:
        del request.session['words_list']
        del request.session['counter']
    except:
        pass
    return redirect('/')
