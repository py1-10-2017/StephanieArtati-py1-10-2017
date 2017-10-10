from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
  return "Hello there! Welcome to my landing page"

@app.route('/ninjas')
def ninja():
  return render_template("ninja.html")

@app.route('/dojos/new')
def add_ninja():
  return render_template("dojos.html")

app.run(debug=True)
