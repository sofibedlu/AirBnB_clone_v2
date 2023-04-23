#!/usr/bin/python3
"""starts flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
import models


app = Flask(__name__)
states = storage.all(State)


@app.teardown_appcontext
def cleanup(exc):
    """remove current sqlalchemy session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def city_state():
    """display html page"""
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
