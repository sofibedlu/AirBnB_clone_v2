#!/usr/bin/python3
"""starts flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
states = storage.all(State)


@app.teardown_appcontext
def cleanup(exc):
    """remove current sqlalchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state():
    """display html page"""
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
