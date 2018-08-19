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
		})
		
	return jsonData

def getAccelAndOrient():

# create empty json objecy
	jsonData = [{}]

	# Date and time of logging
	cursor.execute("SELECT datetime(date_time, 'localtime') FROM accel_and_orient")
	dateTimes = cursor.fetchall()

	'''Acceleromater'''
	# X Acceleration
	cursor.execute("SELECT round(x, 2) FROM accel_and_orient")
	accelX = cursor.fetchall()

	# Y Acceleration
	cursor.execute("SELECT round(y, 2) FROM accel_and_orient")
	accelY = cursor.fetchall()

	# Z
	cursor.execute("SELECT round(z, 2) FROM accel_and_orient")
	accelZ = cursor.fetchall()

	'''Orientation'''
	# Pitch
	cursor.execute("SELECT round(pitch, 2) FROM accel_and_orient")
	pitches = cursor.fetchall()

	# Roll
	cursor.execute("SELECT round(roll, 2) FROM accel_and_orient")
	rolls = cursor.fetchall()

	# Yaw
	cursor.execute("SELECT round(yaw, 2) FROM accel_and_orient")
	yaws = cursor.fetchall()
	
	# iterate through the table adding each row to the json object
	for row in range(len(dateTimes)):
		jsonData.append({
			'date_time': dateTimes[row],
			'x': accelX[row],
			'y': accelY[row],
			'z': accelZ[row],
			'pitch': pitches[row],
			'roll': rolls[row],
			'yaw': yaws[row]
		})
		
	return jsonData

# main route 
@app.route("/")
def index():	
	temp_humid_data = getTempAndHumid()
	accel_orient_data = getAccelAndOrient()
	
	return render_template('index.html',  tempTable = temp_humid_data,
	accelTable = accel_orient_data)

# starts the web server
if __name__ == "__main__":	
	host = os.popen('hostname -I').read()
	app.run(host='10.0.0.58', port=80, debug=False)
