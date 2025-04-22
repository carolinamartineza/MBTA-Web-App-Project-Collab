from flask import Flask, render_template, request
from mbta_helper import find_stop_near, MAPBOX_TOKEN
import sqlite3
from db import init_db
init_db()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/nearest_mbta", methods=["POST"])
def nearest_mbta():
    place = request.form.get("place")

    if not place:
        return render_template("error.html", message="No location provided.")

    result = find_stop_near(place)
    if result:
        station, accessible, lat, lng = result

        conn = sqlite3.connect("mbta.db")
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO searches (place, station, accessible, latitude, longitude)
            VALUES (?, ?, ?, ?, ?)
        """, (place, station, accessible, lat, lng))

        conn.commit()
        conn.close()

        return render_template("mbta_station.html",
                                place=place,
                                station=station,
                                accessible="Yes" if accessible else "No",
                                latitude=lat,
                                longitude=lng,
                                MAPBOX_TOKEN=MAPBOX_TOKEN)
    else:
        return render_template("error.html", message="Could not find a nerby stop.")

@app.route("/history")
def history():
    conn = sqlite3.connect("mbta.db")
    cur = conn.cursor()

    cur.execute("SELECT place, station, accessible, latitude, longitude FROM searches ORDER BY id DESC")
    rows = cur.fetchall()

    conn.close()

    return render_template("history.html", searches=rows)


if __name__ == "__main__":
    app.run(debug=True)