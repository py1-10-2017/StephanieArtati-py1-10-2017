from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'NumberGameAppKey'

@app.route('/',methods=['POST','GET'])
def index():
  if (session.get('number') == None): #if starting a new game
      #get a number to guess and store in session
      session['number'] = random.randrange(0,101)
      #print("Number to be guessed: ",session['number'])
      return render_template("guess.html")
  print("Continuing with checking guess")
  try:
      if (request.form['guess'] != None): #if guessing a game
         target_number = session['number']
         #print(target_number)
         if (int(request.form['guess'])>session['number']):
             #print ("Guess is too high")
             return render_template("guess.html",signal=1) #signal for too high
         elif (int(request.form['guess'])<session['number']):
             #print ("Guess is too low")
             return render_template("guess.html",signal=0) #signal for too low
         else: #guess is right
             session.pop('number')
             return render_template("success.html",number=target_number)
  except:
      return render_template("guess.html")

app.run(debug=True)
