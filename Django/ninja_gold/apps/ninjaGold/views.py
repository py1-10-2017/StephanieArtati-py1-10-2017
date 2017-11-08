from django.shortcuts import render, redirect, HttpResponse
import random, datetime

# Create your views here.
def index(request):
    #initialize session
    if 'score' not in request.session:
        request.session['score'] = 0
        request.session['activities'] = []
    return render(request, "ninjaGold/ninjaGold.html")

def process_money(request, building):
    # building = request.POST['building']
    winning = 0
    timestamp = datetime.datetime.now()
    t_str = timestamp.strftime('%Y/%m/%d %I:%M %p')
    if (building == "farm"):
        winning = random.randrange(10,21)
    elif (building == "cave"):
        winning = random.randrange(5,11)
    elif (building == "house"):
        winning = random.randrange(2,6)
    elif (building == "casino"):
        winning = random.randrange(-50,51)
    request.session['score'] += winning
    #print("Just won",winning,". Running score:",session['score'])
    if (winning >= 0):
        new_activity = {'winning':winning,'building':building,'time':t_str, 'flag':1}
    elif (winning<0):
        winning = abs(winning)
        new_activity = {'winning':winning,'building':building,'time':t_str, 'flag':0}
    request.session['activities'].append(new_activity)
    #print(session['activities'])
    return redirect("/")

def reset_session(request):
    del request.session['score']
    del request.session['activities']
    return redirect("/")
