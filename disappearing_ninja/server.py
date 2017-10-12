from flask import Flask, render_template, request, redirect, session
import random, datetime
app = Flask(__name__)
app.secret_key = 'DisappearingNinjaAppKey'

@app.route('/',methods=['GET'])
def root():
    return "No ninjas here"

@app.route('/ninja/<color>')
def display_ninja(color):
    display_set = []
    if (color == "blue" or color == "orange" or color == "red" or color == "purple"):
        display_set.append(color)
    else:
        display_set.append("other")
    return render_template("ninja.html",display_set=display_set)

@app.route('/ninja')
def display_all():
    display_set = ["blue","orange","red","purple"]
    return render_template("ninja.html",display_set=display_set)
app.run(debug=True)
