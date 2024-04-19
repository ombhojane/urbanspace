from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import google.generativeai as genai
import os
from geopy.geocoders import Nominatim


app = Flask(__name__)
app.secret_key = os.urandom(24)  

API_KEY = os.getenv('GENAI_API_KEY')
genai.configure(api_key=API_KEY)

geolocator = Nominatim(user_agent="urban_green_space_mapping", timeout=10)

@app.route('/get_location')
def get_location():
    city_name = request.args.get('city')
    location = geolocator.geocode(city_name)
    if location:
        return jsonify({'latitude': location.latitude, 'longitude': location.longitude})
    else:
        return jsonify({'latitude': None, 'longitude': None}), 404


@app.route('/visualize')
def visualize():
    return render_template('visualize.html')

@app.route('/')
def index():
    session.clear()  # Clear session at the start
    return render_template('index.html')

@app.route('/predict')
def pedict():
    session.clear()  # Clear session at the start
    return render_template('predict.html')

@app.route('/generate')
def generate():
    session.clear()  # Clear session at the start
    return render_template('generate.html')



if __name__ == '__main__':
    app.run(debug=True)

