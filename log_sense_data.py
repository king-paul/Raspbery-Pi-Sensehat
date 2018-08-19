#!/usr/bin/env python3
# reference: http://yaab-arduino.blogspot.com/2016/08/accurate-temperature-reading-sensehat.html
import datetime
import os
import time

# packages needed for data logging
import sqlite3 as sqlite
from sense_hat import SenseHat

# sense hat package
from sensehat_data import getTemperature, getHumidity, getAcceleration, getOrientation

# databse file
dbFile = '/home/pi/python/assignment1/data_log.db'

# gets the sensed temperature and humidity and creates an SQL statement
def logTempAndHumidity(cursor):

	# get sense hat data from functions
	temp = getTemperature()
	humidity = getHumidity()
	
	cursor.execute("INSERT INTO temp_and_humid VALUES(DATETIME('now'), (?), (?))",
	(temp, humidity))

# gets the sensed acceleration and orientation and creates an SQL statement
def logAccelAndOrient(cursor):
	accel = getAcceleration()
	orient = getOrientation()
	
	cursor.execute("INSERT INTO accel_and_orient " +
	"VALUES(DATETIME('now'), (?), (?), (?), (?), (?), (?))",
	(accel['x'], accel['y'], accel['z'], orient['pitch'], orient['roll'], orient['yaw']))

	print('Accelerometer and Orientation successful')

def main():
	sense = SenseHat()

	# open the database
	connection = sqlite.connect('data_log.db')
	cursor = connection.cursor()

	# log data to SQL query
	logTempAndHumidity(cursor)
	logAccelAndOrient(cursor)

	connection.commit() # commits the sql query
	connection.close() # closes the database

	print('The data has been logged')
	sense.show_message('DATA LOGGED')

main() # starts the program