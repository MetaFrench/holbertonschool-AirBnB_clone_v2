#!/usr/bin/python3
"""Module hello_route
Starts flask web application listening on 0.0.0.0:5000
"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_HBNB():
    """prints Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """prints HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """prints c followed by text value"""
    text = text.replace("_", " ")
    return ("C {}".format(text))


@app.route("/python")
def python_is_cool():
    """prints python is cool"""
    return ("Python is cool")


@app.route("/python/<text>")
def py_text(text):
    """prints Python followed by text value"""
    text = text.replace("_", " ")
    return ("Python {}".format(text))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
