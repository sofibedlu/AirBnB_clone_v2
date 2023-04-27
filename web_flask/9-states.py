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


@app.route('/states', strict_slashes=False)
def state():
    """display html page"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """display html page"""
    """the retrieval of the State objects should be inside the function
    to ensure that the most up-to-date data is being retrieved from the
    database
    """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
