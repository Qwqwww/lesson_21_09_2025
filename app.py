from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=["get", "post"])
def hello():
    message = ""
    if request.method == "POST":
        area = request.form.get("area")
        area = float(area)  # TODO: добавить проверку ввода
        message = f"Площадь квартиры: {area} кв.м."
    return render_template("index.html", message=message)


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
