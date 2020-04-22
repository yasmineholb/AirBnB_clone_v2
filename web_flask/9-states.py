#!/usr/bin/python3
""" start a Flask web app"""
from flask import Flask
from models import storage
from flask import render_template
app = Flask(__name__)



@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(st_id=None):
    """display id"""
    st = storage.all("State")
    if st_id is not None:
        st_id = 'State.' + st_id
    return render_template("9-states.html", states=st, state_id=st_id)


@app.teardown_appcontext
def handle_trd(self):
    """ method to handle teardown """
    storage.close()


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
