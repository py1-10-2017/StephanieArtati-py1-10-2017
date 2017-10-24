from flask import Flask, render_template, redirect, request, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# PASSWORD_REGEX = re.compile(r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'full_friends')
# an example of running a query
print(mysql.query_db("SELECT * FROM friends"))


@app.route('/')
def index():
  friends_list = mysql.query_db("SELECT * FROM friends")
  return render_template("index.html", friends_list=friends_list)

@app.route('/friends', methods=['POST'])
def add_friend():
  email = request.form['email']
  first_name = request.form['first_name']
  last_name = request.form['last_name']

  # inserting new friend into database
  query = "INSERT INTO friends (`first_name`,`last_name`,`email`) VALUES (:first_name, :last_name, :email);"
  data = {'first_name': first_name, 'last_name': last_name, 'email': email}
  new_id = mysql.query_db(query, data)
  friends_list = mysql.query_db("SELECT * FROM friends")
  return render_template("index.html", friends_list=friends_list)

@app.route('/friends/<id>/edit')
def edit_friend(id):

  query = "SELECT * FROM friends where id=:id"
  data = {'id': id}
  friends = mysql.query_db(query, data)
  print("** Finish executing select friend with id: "+id)
  print(friends)
  return render_template("edit_friend.html",  friend=friends[0])

@app.route('/friends/<id>', methods=['POST'])
def update_friend(id):
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    query = "UPDATE friends SET `first_name`=:first_name, `last_name`=:last_name, `email`=:email WHERE `id`=:id";
    data = {'first_name': first_name, 'last_name': last_name, 'email': email, 'id':id}
    mysql.query_db(query, data)
    friends_list = mysql.query_db("SELECT * FROM friends")
    return render_template("index.html", friends_list=friends_list)

@app.route('/friends/<id>/delete', methods=['GET','POST'])
def delete_friend(id):
    query = "DELETE from friends WHERE `id`=:id";
    data = {'id':id}
    mysql.query_db(query, data)
    friends_list = mysql.query_db("SELECT * FROM friends")
    return render_template("index.html", friends_list=friends_list)

@app.route('/reset')
def clear_session():
  session.clear()
  mysql.query_db("DELETE FROM friends")
  return redirect("/")

app.run(debug=True)
