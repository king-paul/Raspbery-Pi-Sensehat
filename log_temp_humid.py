import datetime
import os

# packages needed for data logging
import sqlite3 as sqlite
from crontab import CronTab

# sense hat package
from sense_hat import SenseHat

# databse file
dbFile = 'data_log.db'

# get the sense hat object
sense = SenseHat()

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
	
	# calculate the actual temperature using formula
	air_temp = temp - (cpu_temp - getHumidity()) / factor	
	return air_temp
	
def getHumidity():
	humidity = sense.get_humidity()
	return humidity

# save the sensed temperature and humidity to the database
def logTempAndHumidity(database, time, temp, humidity):
	cursor = database.cursor()

	cursor.execute("INSERT INTO temp_and_humid values(datetime('now'), (?) (?))",
	 (time, temp, humidity,))
	cursor.commit() # commits the sql query
	cursor.close()

	print "The data has been logged."
	
def main():
	# get data from functions
	now = getDateAndTime()
	temp = getTemperature()
	humidity = getHumidity()

	# print the data to the console
	'''print "The current date and time is %s" % now.strftime("%Y-%m-%d %H:%M")
	print "the temperature is %d degrees celsius" % temp
	print "the humidity is %d" % humidity'''

	# open the database
	connection = sqlite.connect('data_log.db')

	logTempAndHumidity(connection, now, temp, humidity)
	
def startCronJob():
	# initialize cron
	cron = CronTab(user = 'pi')
	cron.remove_all()

	# create a new cron job
	job = cron.new(command='main')

	job.minute.every(1) # configure job to run once a minute
	cron.write() # start the cron job

# Begin the program
#startCronJob()
main()