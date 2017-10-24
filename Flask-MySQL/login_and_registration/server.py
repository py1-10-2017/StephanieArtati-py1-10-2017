from flask import Flask, render_template, redirect, request, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
# import the Bcrypt module
from flask_bcrypt import Bcrypt
# import regex
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# PASSWORD_REGEX = re.compile(r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])')

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'KeepItSecretKeepItSafe'
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'registration')
# an example of running a query
print(mysql.query_db("SELECT * FROM users"))


@app.route('/')
def index():
  return render_template("login.html")

@app.route('/process_login', methods=['POST'])
def process_login():
    email = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM users where email=:email"
    data = {'email': email}
    user = mysql.query_db(query, data)
    # If user is found and password match
    if len(user) != 0 and bcrypt.check_password_hash(user[0]['password'], password):
        return render_template("success.html", message="Congratulations, you are logged in")
        session['logged_in'] = True
    else:
        flash("Login failed, please try again")
        return render_template("login.html")

@app.route('/register', methods=['GET'])
def register():
    return render_template("register.html")

@app.route('/process_registration', methods=['POST'])
def process_registration():
  first_name = request.form['first_name']
  last_name = request.form['last_name']
  email = request.form['email']
  password = request.form['password']
  password_confirm = request.form['password_confirm']
  validation = True

  if len(first_name) < 2 or len(last_name) < 2:
      validation = False
      flash("First and last name must be at least 2 characters long")
  if len(password) < 8:
      validation = False
      flash("Password must be at least 8 characters long")
  if password_confirm != password:
      validation = False
      flash("Passwords don't match")
  if not EMAIL_REGEX.match(email):
      validation = False
      flash("Email is not valid!")

  if not validation:
      return render_template("register.html", first_name=first_name, last_name=last_name, email=email)
  pw_hash = bcrypt.generate_password_hash(password)
  query = "INSERT INTO users (`first_name`,`last_name`,`email`,`password`) VALUES (:first_name, :last_name, :email, :passwd_encrypt);"
  data = {'first_name': first_name, 'last_name': last_name, 'email': email, 'passwd_encrypt': pw_hash}
  new_id = mysql.query_db(query, data)
  new_user = mysql.query_db("SELECT * FROM users where id=" + str(new_id))
  session['logged_in'] = True
  return render_template("success.html", message="Congratulations, you are registered   " +new_user[0]['first_name']+"!")

@app.route('/reset')
def clear_session():
  session.clear()
  mysql.query_db("DELETE FROM users")
  return redirect("/")

app.run(debug=True)
