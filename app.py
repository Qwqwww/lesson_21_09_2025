from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello!"


@app.route("/login/", methods=["get", "post"])
def login():
    message = "Место под сообщение"
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username != "123":
            message = "Неправильное имя пользователя"
        else:
            message = f"Имя пользователя: {username}, пароль {password}"
    return render_template("login.html", message=message)


app.run()
