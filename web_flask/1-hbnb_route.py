#!/usr/bin/python3
"""
module for a script that starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello_flask():
    """
    /: display “Hello HBNB!”
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_flask():
    """
    /hbnb: display “HBNB”
    """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
