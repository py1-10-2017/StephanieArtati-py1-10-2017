from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'CounterAppKey'

@app.route('/')
def index():
  try:
    session['counter'] += 1
  except:
    session['counter'] = 1
  return render_template("counter.html")

@app.route('/doubleincrement')
def doubleincrement():
  session['counter'] += 1
  return redirect('/')

@app.route('/reset')
def reset():
  session['counter'] = 0    
  return redirect('/')

app.run(debug=True)
