#Script voor evaluatie 08/11 voormiddag
from flask import Flask
from flask import request
from flask import render_template
import datetime
import folium

microweb_app = Flask(__name__)

@microweb_app.route("/")
def main():
    return render_template("index.html" , datetime_now = datetime.datetime.now())

if __name__ == "__main__":
    microweb_app.run(host="127.0.0.2", port=5050)