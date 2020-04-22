#!/usr/bin/python3
""" start a Flask web app"""
from flask import Flask
from models import storage
from flask import render_template
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_ls():
    """ state list fn"""
    st = storage.all("State").values()
    return render_template("7-states_list.html", states=st)


@app.teardown_appcontext
def handle_trd(self):
    """
        method to handle teardown
    """
    storage.close()


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
