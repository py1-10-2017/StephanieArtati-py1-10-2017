from flask import Flask, render_template, redirect, request, session, flash

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'


@app.route('/')
def index():
  return render_template("registration.html")

@app.route('/reset')
def clear_session():
  session.clear()
  return redirect("/")

@app.route('/process_registration', methods=['POST'])
def process_registration():
  email = request.form['email']
  first_name = request.form['first_name']
  last_name = request.form['last_name']
  password = request.form['password']
  confirm_password = request.form['confirm_password']
  validation = True
  if len(first_name)<1 or len(last_name)<1:
      flash("First name and last name cannot be empty")
      validation = False

  if len(email)<1:
      flash("Email cannot be empty")
      validation = False
  elif not EMAIL_REGEX.match(email):
      flash("Invalid Email Address!")

  if len(password) < 8:
      flash("Password must be at least 8 characters")
      validation = False
  if password.isalpha() or password.isnumeric():
      flash("Password must contain at least 1 alphabet and 1 numeric characters")
      validation = False
  if password.islower() or password.isupper():
       flash("Password must contain at least 1 uppercase and 1 lowercase character")
       validation = False
  if password != confirm_password:
      flash("Passwords don't match")
      validation = False

  if not validation:
      return render_template("registration.html", email=email, first_name=first_name, last_name=last_name)
  return render_template("success.html")

app.run(debug=True)
