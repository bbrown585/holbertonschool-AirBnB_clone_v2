#!/usr/bin/python3
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/')
def index():
    """ display “Hello HBNB!" """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ define route /hbnb and return a text"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """Returns a string starting with C"""
    mod_text = escape(text)
    return 'C %s' % mod_text.replace("_", " ")


if __name__ == "__main__":
    """document for main"""
    app.run()
