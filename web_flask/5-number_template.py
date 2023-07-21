#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello_flask():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_flask():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_is_fun(text):
    return 'C %s' % text.replace("_", " ")


@app.route('/python', strict_slashes=False)
def display_python_is():
    return 'Python is cool'


@app.route('/python/<text>', strict_slashes=False)
def display_python_is_magic(text='is_cool'):
    return 'Python %s' % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def display_int_only(n):
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_template(n=None):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
