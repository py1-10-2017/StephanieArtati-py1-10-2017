from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'


@app.route('/')
def index():
  return render_template("dojo_survey.html")

@app.route('/reset')
def clear_session():
  session.clear()
  return redirect("/")

@app.route('/result', methods=['POST'])
def display_result():
  name = request.form['name']
  location = request.form['location']
  language = request.form['language']
  comment = request.form['comment']
  validation = True
  if len(name) < 1:
      flash("Name cannot be empty")
      validation = False
  if len(comment) < 1 or len(comment) > 120:
      flash("Comment cannot be empty and must be within 120 characters long")
      validation = False
  if not validation:
      return render_template("dojo_survey.html", name=name, comment=comment)
  return render_template("result.html", name=name, location=location, language=language, comment=comment)

app.run(debug=True)
