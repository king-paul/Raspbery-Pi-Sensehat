import sqlite3
import datetime
import os
from sense_hat import SenseHat

# get the database file
dbfile = 'data_log.db'
# get the sense hat object
sense = SenseHat()

# get data from SenseHat sensor

# returns the local date and time on the system
def getDateAndTime():
	return datetime.datetime.now()
	
def getTemperature():
	temp = sense.get_temperature()
	factor = 2	
	
	# calibrate temperature
	'''cpu_temp_string = (os.popen('/sys/class/thermal/thermal_zone0/temp').readline())
	print 'CPU temperature: %s' % cpu_temp_string'''
	
	cpu_temp = 45.1 
	'''int(cpu_temp_string)'''
	
	air_temp = temp - (cpu_temp - getHumidity()) / factor
	
	return air_temp
	
def getHumidity():
	humidity = sense.get_humidity()
	return humidity
	
def main():
	# get data from functions
	now = getDateAndTime()
	temp = getTemperature()
	humidity = getHumidity()

	# print the data to the console
	print "The current date and time is %s" % now.strftime("%Y-%m-%d %H:%M")
	print "the temperature is %d degrees celsius" % temp
	print "the humidity is %d" % humidity
	
# Begin the program
main()