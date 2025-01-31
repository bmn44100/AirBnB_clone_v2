#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
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


@app.route('/number_odd_or_even/<int:n>')
def display_odd_or_even(n):
    if n % 2 == 0:
        num = 'even'
    else:
        num = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, num=num)


@app.route('/states_list', strict_slashes=False)
def display_states():
    states = storage.all(State)
    print(states)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def display_teardown(exeption):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
