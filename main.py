from flask import Flask, redirect, url_for, render_template, request
from json import load, dump
from typing import Optional


app = Flask(__name__, "/static/")


@app.route("/checkregister", methods=["GET"])
@app.route("/checklogin", methods=["GET"])
@app.route("/")
def home():
    """
    Redirects to login page.
    """
    return redirect(url_for("login"))


with open("login.html") as file:
    login_html: str = file.read()

with open("register.html") as file:
    register_html: str = file.read()

with open("home.html") as file:
    home_html: list[str] = file.readlines()

with open("users.json") as file:
    users: list[dict[str, str]] = load(file)


@app.route("/login.html")
def login() -> str:
    """
    Returns login page.
    """
    return login_html


register_html_func = lambda: register_html
app.route("/register.html", methods=["GET"], endpoint="fun25x")(register_html_func)


def create_user(username: str, password: str) -> None:
    """
    Creates a new user.

    Args:
        username (str): Username.
        password (str): Password.
    """
    users.append({"username": username, "password": password})
    with open("users.json", "w") as file:
        dump(users, file)


def remove_user(username: str, password: str) -> None:
    """
    Removes a user.

    Args:
        username (str): Username.
        password (str): Password.
    """
    for user in users:
        if user["username"] == username and user["password"] == password:
            users.remove(user)
            with open("users.json", "w") as file:
                dump(users, file)


@app.route("/checklogin", methods=["POST"])
def checklogin() -> Optional[str]:
    """
    Checks login credentials.

    Returns:
        str: Redirect response.
    """
    username = request.form["username"].lower()
    password = request.form["password"]

    for user in users:
        if user["username"] == username:
            if user["password"] == password:
                return home_page(username)
            else:
                return redirect(url_for("login", credentials="invalid_password"))

    return redirect(url_for("login", credentials="invalid"))


@app.route("/checkregister", methods=["POST"])
def checkregister() -> None:
    """
    Checks register credentials.

    Returns:
        str: Redirect response.
    """
    username = request.form["username"].lower()
    password = request.form["password"]

    for user in users:
        if user["username"] == username:
            return redirect(url_for("register", credentials="invalid_exists"))

    create_user(username, password)
    return redirect(url_for("login"))


login_redirect = lambda: redirect(url_for("login"))
app.route("/home", methods=["GET"], endpoint="func12")(login_redirect)


def home_page(username: str = None) -> str:
    """
    Returns home page.

    Args:
        username (str): Username.

    Returns:
        Home page HTML.
    """
    home_html[9] = f"<label style=\"font: 2em sans-serif;\">Welcome, {username}!</label><br><br>"
    return "".join(home_html)


if __name__ == '__main__':
    app.run(debug=True, port=8000)