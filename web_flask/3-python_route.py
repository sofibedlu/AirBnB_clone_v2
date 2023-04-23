#!/usr/bin/python3
"""starts a flask web application"""
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """display 'hello hbnb!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cfun(text):
    """evaluate variable"""
    text = escape(text)
    new = ''
    for i in text:
        if i == '_':
            i = ' '
        new += i
    return "C {}".format(new)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """display python {text}"""
    text = escape(text)
    new = ''
    for i in text:
        if i == '_':
            i = ' '
        new += i
    return "Python {}".format(new)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
