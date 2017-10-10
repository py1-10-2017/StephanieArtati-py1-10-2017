from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'CounterAppKey'

@app.route('/')
def index():
  print("Beginning of root handler")
  if (session.get('counter') != None):
    print("Incrementing counter")
    curr_counter = int(session['counter'])
    session['counter'] = curr_counter + 1
  else:
    print("Initializing counter")
    session['counter'] = "1"
  return render_template("counter.html")

@app.route('/doubleincrement')
def doubleincrement():
  session['counter'] = int(session['counter']) + 1
  return redirect('/')

@app.route('/reset')
def reset():
  session['counter'] = "0"
  return redirect('/')

app.run(debug=True)
