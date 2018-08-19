'''
This script contains functions that read from each of the database table and
convert the returned results into json format before returning a json object
'''
import sqlite3

# start the databse connection
connection = sqlite3.connect('data_log.db')
cursor = connection.cursor()

# returns the date, time, tempurature and humidity in JSON format
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

# returns the date, time, accelerometer and orientation data in JSON format
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

# returns the address and name of bluetooth devices found using bluetooh
# greeting script and returns them in JSON format
def getBluetoothDevices():

	# create empty json objecy
	jsonData = [{}]

	# Date and time of logging
	cursor.execute("SELECT datetime(date_time, 'localtime') FROM bluetooth_devices")
	dateTimes = cursor.fetchall()

	# device address
	cursor.execute("SELECT mac_address FROM bluetooth_devices")
	addresses = cursor.fetchall()

	# device name
	cursor.execute("SELECT device_name FROM bluetooth_devices")
	names = cursor.fetchall()

	# iterate through the table adding each row to the json object
	for row in range(len(dateTimes)):
		jsonData.append({
			'date_time': dateTimes[row],
			'address': addresses[row],
			'name': names[row]
		})

	return jsonData