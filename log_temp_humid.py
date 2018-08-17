#!/usr/bin/env python3
import datetime
import os

# packages needed for data logging
import sqlite3 as sqlite

# sense hat package
from sense_hat import SenseHat

# databse file
dbFile = '/home/pi/python/assignment1/data_log.db'

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

# save the sensed temperature and humidity to the database
def logTempAndHumidity(temp, humidity):
	# open the database
	connection = sqlite.connect('data_log.db')
	cursor = connection.cursor()

	cursor.execute("INSERT INTO temp_and_humid values(datetime('now'), (?), (?))", (temp, humidity))
	connection.commit() # commits the sql query
	connection.close()

	print('The data has been logged.')
	sense.show_message('DATA LOGGED')

def main():
	# get data from functions
	now = getDateAndTime()
	temp = getTemperature()
	humidity = getHumidity()

	# print the data to the console
	'''print('The current date and time is {}'.format(now.strftime("%Y-%m-%d %H:%M")))
	print('the temperature is {} degrees celsius'.format(temp))
	print('the humidity is {}'.format(humidity))'''

	logTempAndHumidity(temp, humidity)
	
def startCronJob():
	# initialize cron
	cron = CronTab(user = 'pi')
	cron.remove_all()

	# create a new cron job
	job = cron.new(command='main')

	job.minute.every(1) # configure job to run once a minute
	cron.write() # start the cron job

	print('Cron job started.')

# Begin the program
#startCronJob()
main()
