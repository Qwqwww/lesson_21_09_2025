from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello!"


@app.route("/login/", methods=["get", "post"])
def login():
    message = "Место под сообщение"
    return render_template("login.html", message=message)


app.run()
