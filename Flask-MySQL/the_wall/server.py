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
mysql = MySQLConnector(app, 'wall_database')
# an example of running a query
print(mysql.query_db("SELECT * FROM users"))


@app.route('/')
def index():
    if 'logged_in' not in session or session['logged_in'] == False:
        return render_template("login.html")
    else:
        # if logged in then build the wall
        messages = mysql.query_db("SELECT * FROM messages ORDER BY created_at DESC")
        for message in messages:
            creator_id = message['user_id']
            query = "SELECT * FROM users where id=:user_id"
            data = {'user_id': creator_id}
            user = mysql.query_db(query, data)
            message['creator_first_name'] = user[0]['first_name']
            message['creator_last_name'] = user[0]['last_name']
            message['created_date'] = message['created_at'].strftime('%B %d %Y')
            query = "SELECT * FROM comments where message_id=:message_id ORDER BY created_at"
            data = {'message_id': message['id']}
            comments = mysql.query_db(query, data)
            for comment in comments:
                creator_id = comment['user_id']
                query = "SELECT * FROM users where id=:user_id"
                data = {'user_id': creator_id}
                user = mysql.query_db(query, data)
                comment['creator_first_name'] = user[0]['first_name']
                comment['creator_last_name'] = user[0]['last_name']
                comment['created_date'] = comment['created_at'].strftime('%B %d %Y')
            message['comments'] = comments

        return render_template("wall.html",messages_list=messages)

@app.route('/post_message', methods=['POST'])
def post_message():
    query = "INSERT INTO messages (`message`,`user_id`,`created_at`,`updated_at`) VALUES (:message, :user_id, now(), now());"
    data = {'message': request.form['message'], 'user_id': session['user_id']}
    new_message = mysql.query_db(query, data)
    return redirect('/')

@app.route('/post_comment', methods=['POST'])
def post_comment():
    query = "INSERT INTO comments (`comment`,`user_id`,`message_id`,`created_at`,`updated_at`) VALUES (:comment, :user_id, :message_id, now(), now());"
    data = {'comment': request.form['comment'], 'user_id': session['user_id'], 'message_id': request.form['message_id']}
    new_message = mysql.query_db(query, data)
    return redirect('/')

@app.route('/process_login', methods=['POST'])
def process_login():
    email = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM users where email=:email"
    data = {'email': email}
    user = mysql.query_db(query, data)
    # If user is found and password match
    if len(user) != 0 and bcrypt.check_password_hash(user[0]['password'], password):
        session['logged_in'] = True
        session['user_id'] = user[0]['id']
        session['user_first_name'] = user[0]['first_name']
        session['user_last_name'] = user[0]['last_name']
        return redirect('/')
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
  query = "INSERT INTO users (`first_name`,`last_name`,`email`,`password`,`created_at`,`updated_at`) VALUES (:first_name, :last_name, :email, :passwd_encrypt, now(), now());"
  data = {'first_name': first_name, 'last_name': last_name, 'email': email, 'passwd_encrypt': pw_hash}
  new_id = mysql.query_db(query, data)
  new_user = mysql.query_db("SELECT * FROM users where id=" + str(new_id))
  session['logged_in'] = True
  session['user_id'] = new_user[0]['id']
  session['user_first_name'] = new_user[0]['first_name']
  session['user_last_name'] = new_user[0]['last_name']
  return redirect('/')

@app.route('/logout')
def clear_session():
  session.clear()
  return redirect("/")

@app.route('/reset')
def clear_all():
  session.clear()
  mysql.query_db("DELETE FROM users")
  return redirect("/")

app.run(debug=True)
