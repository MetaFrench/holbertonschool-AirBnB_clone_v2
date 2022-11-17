#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
import models
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(content):
    """ removes current SQLAlchemy sesh """
    models.storage.close()


@app.route('/states')
@app.route('/states/<id>')
def states_id_route(id=None):
    """ displays HTML for states w state id """
    states = models.storage.all(State)
    return render_template('9-states.html', state_list=states, id=id)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
