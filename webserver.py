#!/usr/bin/env python3
import os
from flask import Flask, render_template
from sense_hat import SenseHat
import json
import sqlite3

# start the databse connection
connection = sqlite3.connect('data_log.db')
cursor = connection.cursor()

app = Flask(__name__)

def getTempAndHumid():

	# create empty json objecy
	jsonData = [{}]

	# retuen first column from table
	cursor.execute("SELECT datetime(date_time, 'localtime') FROM temp_and_humid")
	dateTimes = cursor.fetchall()
	
	# return second column from table
	cursor.execute("SELECT round(temperature, 2) FROM temp_and_humid")
	temps = cursor.fetchall()

	# return third colum from table
	cursor.execute("SELECT  round(humidity, 2) FROM temp_and_humid")
	humids = cursor.fetchall()

	# iterate through the table adding each row to the json object
	for row in range(len(dateTimes)):
		jsonData.append({
			'date_time': dateTimes[row],
			'temperature': temps[row],
			'humidity': humids[row]
		}
		)
		
	return jsonData

# main route 
@app.route("/")
def index():	
	data = getTempAndHumid()
	
	return render_template('index.html',  rows=data)

# starts the web server
if __name__ == "__main__":	
	host = os.popen('hostname -I').read()
	app.run(host='10.0.0.58', port=80, debug=False)
