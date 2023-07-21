#!/usr/bin/python3
# a script that starts a Flask web flaskapplication

from flask import Flask
flaskapp = Flask(__name__)


@flaskapp.route('/', strict_slashes=False)
def display_hello_flask():
    return 'Hello HBNB!'


@flaskapp.route('/hbnb', strict_slashes=False)
def display_flask():
    return 'HBNB'

if __name__ == "__main__":
    flaskapp.run(host="0.0.0.0")
