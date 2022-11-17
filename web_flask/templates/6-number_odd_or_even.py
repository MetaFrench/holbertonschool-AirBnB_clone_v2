#!/usr/bin/python3
"""Module number_route
Starts flask web application listening on 0.0.0.0:5000
Route /number/<n>
"""

from flask import Flask, render_template


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
def py_text(text="is cool"):
    """prints Python followed by text value"""
    text = text.replace("_", " ")
    return ("Python {}".format(text))


@app.route("/number/<int:n>")
def print_int(n):
    """Prints n if n is integer"""
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>")
def int_html(n):
    """returns HTML page if n is integer"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>")
def even_odd_html(n):
    """returns HTML page if n is integer"""
    if ((n % 2)) == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    return render_template('6-number_odd_or_even.html', n=n,
                           even_or_odd=even_or_odd)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
