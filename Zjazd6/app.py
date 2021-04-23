import os
from flask import(
    Flask, render_template,request,session,redirect,url_for,)

app= Flask(__name__)

directory="."

@app.route("/")
def root():

    ls=os.listdir(directory)
    return render_template("Home.html",ls=ls,directory=directory)
