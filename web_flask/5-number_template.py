#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns 'Hello HBNB' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Returns 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ Returns C and changes undercore to blank space """
    text = text.replace('_', ' ')
    return ('C {}'.format(text))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_route(text='is cool'):
    """ Returns Python, value of text,
    and changes underscore to blank space """
    text = text.replace('_', ' ')
    return ('Python {}'.format(text))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ Returns n as a number if n is integer """
    return ('{} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_page(n):
    """ Displays an html page """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
