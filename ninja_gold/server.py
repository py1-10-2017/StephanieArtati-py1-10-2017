from flask import Flask, render_template, request, redirect, session
import random, datetime
app = Flask(__name__)
app.secret_key = 'NumberGameAppKey'

@app.route('/',methods=['GET'])
def index():
    #initialize session
    if 'score' not in session:
        session['score'] = 0
        session['activities'] = []
    return render_template("ninja_gold.html")

@app.route('/process_money',methods=['POST','GET'])
def process_money():
    building = request.form['building']
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
    session['score'] += winning
    #print("Just won",winning,". Running score:",session['score'])
    if (winning >= 0):
        new_activity = {'winning':winning,'building':building,'time':t_str, 'flag':1}
    elif (winning<0):
        winning = abs(winning)
        new_activity = {'winning':winning,'building':building,'time':t_str, 'flag':0}
    session['activities'].append(new_activity)
    #print(session['activities'])
    return redirect("/")

@app.route('/reset')
def reset_session():
    session.clear()
    return redirect("/")

app.run(debug=True)
