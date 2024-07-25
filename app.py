from flask import Flask, jsonify, render_template, abort
import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from station import get_station_info, Station

# TODO

app = Flask(__name__)
stations = get_station_info()

# Format the data to be used in the JavaScript
# Example Use in js:
# const data = [
#     { lat: 51.5175026, lng: -0.1155505, name: "London EV Station 1" },
#     { lat: 51.5198218, lng: -0.1165645, name: "London EV Station 2" },
#     { lat: 51.5155425, lng: -0.1164858, name: "London EV Station 3" }
# ];

# extract only the necessary data
formatted_data = [
    {
        "lat": float(station[5].split(", ")[0]),
        "lng": float(station[5].split(", ")[1]),
        "name": station[1],
        "address": station[6]
    } for station in stations
]

# Convert list of dictionaries to a JSON string
js_data = json.dumps(formatted_data)

# Prepare the string to be written into a .js file
js_output = f"{js_data}"

# Write to a .js file
with open("./project/static/data.json", "w") as js_file:
    js_file.write(js_output)

print(stations)

@app.route("/")
def index():
    return render_template("home.html")

app.run(debug=True)
