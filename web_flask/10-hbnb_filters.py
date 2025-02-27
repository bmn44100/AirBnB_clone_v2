#!/usr/bin/python3
"""
module for a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


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


@app.route('/cities_by_states', strict_slashes=False)
def display_by_states():
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_states_id(id=None):
    states = storage.all(State)
    title = "States"
    if id is not None:
        for items in states.values():
            if id == items.id:
                states = items
                title = "State: {}".format(items.name)
                break
            else:
                title = "Not found!"
    return render_template('9-states.html', states=states, id=id, title=title)


@app.route('/hbnb_filters', strict_slashes=False)
def display_hbnb():
    states = storage.all(State)
    amenity = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=states, amenity=amenity)


@app.teardown_appcontext
def display_teardown(exeption):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
