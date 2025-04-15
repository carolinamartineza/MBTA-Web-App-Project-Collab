from flask import Flask, render_template, request
from mbta_helper import find_stop_near, MAPBOX_TOKEN

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        place = request.form["place"]
        data = find_stop_near(place)
        if data:
            station, accessible, lat, lng = data
            result = {
                "place": place,
                "station": station,
                "accessible": "Yes" if accessible else "No",
                "latitude": lat,
                "longitude": lng
            }
        else:
            result = {"error": "Could not find a nearby station."}
    return render_template("index.html", result=result, MAPBOX_TOKEN=MAPBOX_TOKEN)

if __name__ == "__main__":
    app.run(debug=True)