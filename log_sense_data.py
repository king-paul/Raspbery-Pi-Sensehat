#!/usr/bin/env python3
import datetime
import os

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
       # return 0

def getTemperature():
	temp = sense.get_temperature_from_humidity()
	factor = 1.5	
	
	# calibrate temperature
	cpu_temp =  getCpuTemperature()
	#print ('CPU temperature: {}'.format(cpu_temp))
		
	# calculate the actual temperature using formula
	air_temp = temp - (cpu_temp - temp) / factor

	return air_temp
	
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

# Begin the program
main()
