from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
from pollution_tracker import track_route_and_pollution

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        origin = request.form.get("origin")
        destination = request.form.get("destination")

        average_air_quality, route_data, waypoints = track_route_and_pollution(origin, destination)

        result = {
            "average_air_quality": average_air_quality,
            "directions_result": route_data["directions_result"],
            "waypoints": route_data["waypoints"]
        }
        return json.dumps(result)  # Replace 'jsonify(result)' with 'json.dumps(result)'

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
