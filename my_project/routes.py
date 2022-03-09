from my_project import app, render_template
from my_project.models import User
from flask import request, jsonify, make_response, redirect, url_for
from my_project import db

@app.route("/", methods=["GET"])
def index():
    context = {}
    if 'userID' in request.cookies:
        user = User.query.filter_by(email=request.cookies.get('userID')).first()
        context["loggedin"] = True
        context["email"] = user.name
    return render_template("index.html", **context)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        context = {}
        email = request.form['email']
        pwd = request.form['pwd']
    
        user = User.query.filter_by(email=email, pwd=pwd).first()
        if user:
            context["loggedin"] = True
            context["user"] = user.name

            context["error"] = False
            resp = make_response(render_template("index.html", **context))
            resp.set_cookie("userID", email)
            return resp
        else:
            context["error"] = True
            context["error_text"] = "User already present!"
            return render_template("login.html", **context)
    return render_template("login.html")

@app.route("/logout", methods=["GET"])
def logout():
    if 'userID' in request.cookies:
        context={}
        resp = make_response(render_template("index.html", **context))
        resp.set_cookie("userID", expires=0)
        return resp
    return redirect(url_for("index"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    context = {}
    if request.method == 'POST':
        print(request.form)
        name = request.form['name']
        contact_no = request.form['contact_no']
        email = request.form['email']
        pwd = request.form['pwd']

        user = User.query.filter_by(email=email).first()
        if user:
            context["error"] = True
            context["error_text"] = "User already present!"
            return render_template("signup.html", **context)
        else:
            user = User(name=name, contact_no=contact_no, email=email, pwd=pwd)
            db.session.add(user)
            db.session.commit()

            context["error"] = False
            context["error_text"] = "User successfully created!"
            return render_template("signup.html", **context)
    return render_template("signup.html")

@app.route("/predict", methods=["POST"])
def predict():
    # all prediction will be done here
    return render_template("predict.html")