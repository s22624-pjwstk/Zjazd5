import os
from flask import(
    Flask, render_template,request,session,redirect,url_for,)

app= Flask(__name__)

ROOT_DIRECTORY="."
x={1:1,2:2}

def render_listing(directory):
    ls = os.listdir(directory)
    ls_directory = []
    ls_file = []
    for x in ls:
        if os.path.isdir(x):
            ls_directory.append({"url": x, "name": x})
        else:
            ls_file.append(x)

    return render_template("Home.html", ls_directory=ls_directory, ls_file=ls_file, directory=directory)

@app.route("/")
def root():
    directory=""
    if directory =="":
        directory=ROOT_DIRECTORY

    return render_listing(directory)

@app.route("/<path:directory>")
def ls(directory):
    return render_listing(directory)