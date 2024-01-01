#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, abort

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    route displaying "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    route displaying "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Route that displays "C ", followed by the value of the text variable
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Route displaying "n is a number" only if n is an integer
    """
    return "{} is a number".format(n)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    Route that displays "Python ", followed by the value of the text variable)
    Default value for text is "is cool"
    """
    return "Python {}".format(text.replace('_', ' '))


@app.errorhandler(404)
def not_found(error):
    """
    404 errors by returning a custom response
    """
    return "Not Found", 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
