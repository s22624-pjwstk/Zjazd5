import os
from flask import(
    Flask, render_template,request,session,redirect,url_for,)

app= Flask(__name__)

ROOT_DIRECTORY=os.path.abspath(".")
x={1:1,2:2}


def render_listing(directory):
    print(directory)
    parent_directory=os.path.join(directory,"..")
    parent_directory=os.path.normpath(parent_directory)
    print(parent_directory)
    ls_raw = os.listdir(directory)
    ls_raw.append("..")
    ls=[]
    for i in ls_raw:
        ls_new=os.path.join(directory,i)
        ls_new=os.path.normpath(ls_new)

        ls.append(ls_new)

    print(ls_raw)
    print(ls)
    ls_directory =[]
    ls_file = []
    for x in ls_raw:
        ls_new = x.replace(ROOT_DIRECTORY, "")
        if os.path.isdir(x):
            href=ls_new.replace("\\","/")
            ls_directory.append({"href": href, "name":x})
            print(x)
        else:
            ls_file.append(x)


    return render_template("Home.html", ls_directory=ls_directory, ls_file=ls_file, directory=directory)

@app.route("/")
def root():
    print(ROOT_DIRECTORY)
    return render_listing(ROOT_DIRECTORY)

@app.route("/<path:directory>")
def ls(directory):
    return render_listing(directory)