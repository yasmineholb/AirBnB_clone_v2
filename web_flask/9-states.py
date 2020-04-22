#!/usr/bin/python3
""" start a Flask web app"""
from flask import Flask
from models import storage
from flask import render_template
app = Flask(__name__)



@app.route('/states', strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Display htm id"""
    for st in storage.all("State").values():
        if st.id == id:
            return render_template("9-states.html", state=st)
    return render_template("9-states.html")


@app.teardown_appcontext
def handle_trd(self):
    """ method to handle teardown """
    storage.close()


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
