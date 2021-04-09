from flask import(
    Flask, render_template,request,session,redirect,url_for)

app = Flask(__name__)
USERS=[
    ("Karas",124),
    ("Krystain",125),
    ("Tomek",126)
]

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/calculator/<string:op>/<float:lhs>/<float:rhs>',methods=("GET","POST"),)
def calculator(op,lhs,rhs):
    l=lhs
    r=rhs
    znak=op
    wynik=0
    if (l==0 or r==0 and znak==":"):
        wynik=0
    else:
        if(znak=="+"):
            wynik=l+r
        elif(znak=="-"):
            wynik=l-r
        elif(znak==":"):
            wynik=l/r
        elif(znak=="*"):
            wynik=l*r
    return str(wynik)
@app.route("/users/<int:user_id>")
def user(user_id):
    x=[x for x in USERS if x[1]==user_id]
    if x:
        return str(x[0])
    else:
        return "Nie ma takiego użytkownika"


if __name__ == '__main__':
    app.run(debug=True)
