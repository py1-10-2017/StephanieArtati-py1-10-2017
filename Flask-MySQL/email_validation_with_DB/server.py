from flask import Flask, render_template, redirect, request, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# PASSWORD_REGEX = re.compile(r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'email_database')
# an example of running a query
print(mysql.query_db("SELECT * FROM users"))


@app.route('/')
def index():
  return render_template("index.html")

@app.route('/reset')
def clear_session():
  session.clear()
  mysql.query_db("DELETE FROM users")
  return redirect("/")

@app.route('/process_registration', methods=['POST'])
def process_registration():
  email = request.form['email']
  validation = True

  if not EMAIL_REGEX.match(email):
      validation = False
      flash("Email is not valid!")

  if not validation:
      return render_template("index.html", email=email)
  query = "INSERT INTO `email_database`.`users` (`email`, `created_at`) VALUES (:email, now());"
  data = {'email': email}
  new_id = mysql.query_db(query, data)
  email_list = mysql.query_db("SELECT * FROM users")
  return render_template("success.html", email=email, email_list=email_list)

app.run(debug=True)
