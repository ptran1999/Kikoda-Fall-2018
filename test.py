from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
	zipcode = request.form['zip']
	r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=f833e67ae1e9e2c2f52f984f548ba1b2')
	json_object = r.json()
	temp_k = float(json_object['main']['temp'])
	temp_c = (temp_k - 273.15)
	return render_template('temperature.html', temp=temp_c)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)