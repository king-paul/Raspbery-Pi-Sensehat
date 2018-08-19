#!/usr/bin/env python3
# reference: http://yaab-arduino.blogspot.com/2016/08/accurate-temperature-reading-sensehat.html
import datetime
import os
import time

# packages needed for data logging
import sqlite3 as sqlite

# sense hat package
from sense_hat import SenseHat

# databse file
dbFile = '/home/pi/python/assignment1/data_log.db'

# open the database
connection = sqlite.connect('data_log.db')
cursor = connection.cursor()

# get the sense hat object
sense = SenseHat()
# returns the local date and time on the system
def getDateAndTime():
	return datetime.datetime.now()

def getCpuTemperature():
    
	cpu_temp_string = os.popen("vcgencmd measure_temp").readline()
	cpu_temp = float(cpu_temp_string.replace("temp=","").replace("'C\n",""))
	return(cpu_temp)

def getTemperature():
	temp = sense.get_temperature_from_humidity()
	factor = 1.2 # this number seems to get the most acurate result	
	
	# calibrate temperature
	cpu_temp =  getCpuTemperature()
		
	# calculate the actual temperature using formula
	air_temp = temp - (cpu_temp - temp) / factor
	
	return air_temp
	
def smoothTemperature(temp, timeLength):
	# get the average of fluctuating temperatures
	secs = 0
	while secs < timeLength:
		temp = get_smooth(temp) 
		time.sleep(1)
		secs +=1

	return temp

# use moving average to smooth readings
# reference: http://yaab-arduino.blogspot.com/2016/08/accurate-temperature-reading-sensehat.html
def get_smooth(x):

	print('Smoothing out temperatures..')

	if not hasattr(get_smooth, "t"):
		get_smooth.t = [x,x,x]

	get_smooth.t[2] = get_smooth.t[1]
	get_smooth.t[1] = get_smooth.t[0]
	get_smooth.t[0] = x
	xs = (get_smooth.t[0]+get_smooth.t[1]+get_smooth.t[2])/3

	return(xs)
	
def getHumidity():
	humidity = sense.get_humidity()
	return humidity

def logAccelAndOrient():
	accel = sense.get_accelerometer_raw()
	orient = sense.get_orientation()
	
	cursor.execute("INSERT INTO accel_and_orient " +
	"VALUES(DATETIME('now'), (?), (?), (?), (?), (?), (?))",
	(accel['x'], accel['y'], accel['z'], orient['pitch'], orient['roll'], orient['yaw']))

	print('Accelerometer and Orientation successful')

# save the sensed temperature and humidity to the database
def logTempAndHumidity(temp, humidity):
	
	cursor.execute("INSERT INTO temp_and_humid VALUES(DATETIME('now'), (?), (?))",
	(temp, humidity))

def main():
	# get sense hat data from functions
	temp = getTemperature()
	humidity = getHumidity()

	logTempAndHumidity(temp, humidity)
	logAccelAndOrient()

	connection.commit() # commits the sql query
	connection.close()

	print('The data has been logged')
	sense.show_message('DATA LOGGED')