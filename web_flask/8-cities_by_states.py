#!/usr/bin/python3
""" Flask Routing Template """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states',  strict_slashes=False)
def display_cities():
    """ retrieve list of states and passes to template"""
    states_list = []
    dic_states = storage.all(State)
    for state in dic_states.values():
        states_list.append(state)
    return render_template('8-cities_by_states.html', states=states_list)


@app.teardown_appcontext
def teardown_db(exception):
    '''close connections'''
    storage.close()

if __name__ == "__main__":
    app.run()
