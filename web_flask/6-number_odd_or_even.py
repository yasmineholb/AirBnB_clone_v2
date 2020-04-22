#!/usr/bin/python3
""" start a Flask web app"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ fn web app """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ fn web app """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hb_text(txt):
    """ fn web app """
    return "C {}".format(txt.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/(<text>)', strict_slashes=False)
def hb_textpy(txt="is cool"):
    """ fn web app """
    return "Python {}".format(txt.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def hb_numb(n):
    """ fn web app """
    if int(n) is True:
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def hb_html(n):
    """ fn web app """
    if int(n) is True:
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def hb_html(n):
    """ fn web app """
    if int(n) is True:
        return render_template("6-number_odd_or_even.html", n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
