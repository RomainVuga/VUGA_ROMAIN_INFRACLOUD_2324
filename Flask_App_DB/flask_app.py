from flask import Flask, app
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash
import sqlite3
import datetime
import folium

microweb_app = Flask(__name__)
app.secret_key = '\xf0?a\x9a\\\xff\xd4;\x0c\xcbHi'

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

@microweb_app.route("/time")
def time():
    return render_template("time.html")

@microweb_app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

    flash('Account created successfully! Please log in.', 'success')
    return redirect(url_for('main'))

@microweb_app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and(user[2], password):
        flash('Login successful!', 'success')
    else:
        flash('Login failed. Please check your username and password.', 'danger')

    return redirect(url_for('main'))

if __name__ == "__main__":
    microweb_app.run(host="127.0.0.1", port=5555)