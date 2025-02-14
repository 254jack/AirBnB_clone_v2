#!/usr/bin/python3
# Python script that starts a flask application on 0.0.0.0 port 5000/
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def teardown_app(exception):
    """invokes Storage close on appcontext"""
    storage.close()


@app.route('/new_filters')
def new_filter():
    states = []
    for key, values in storage.all('State').items():
        states.append(values)
    cities = []
    for key, values in storage.all('City').items():
        cities.append(values)
    amenities = []
    for key, values in storage.all('Amenity').items():
        amenities.append(values)
    return render_template('10-new_filters.html', states=states,
                           cities=cities, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
