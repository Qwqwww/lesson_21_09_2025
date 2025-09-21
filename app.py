from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello!"


@app.route("/login/", methods=["get", "post"])
def login():
    return render_template("login.html")


app.run()
