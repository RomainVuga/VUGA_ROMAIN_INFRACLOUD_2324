from flask import Flask
from flask import request
from flask import render_template
import datetime
import folium

microweb_app = Flask(__name__)

@microweb_app.route("/")
def main():
    return render_template("index.html" , datetime_now = datetime.datetime.now())

@microweb_app.route("/map")
def map():
    # Create a map centered on Brussels
    m = folium.Map(location=[50.8503, 4.3517], zoom_start=13)

    # Add a marker at the center of Brussels
    folium.Marker(location=[50.8503, 4.3517], popup='Brussels').add_to(m)

    # Render the map
    map_html = m.get_root().render()

    # Create an HTML template with the map
    return render_template('map.html', map_html=map_html)

if __name__ == "__main__":
    microweb_app.run(host="127.0.0.1", port=5050)