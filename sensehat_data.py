'''
This file contains all the functions neededed to read data from the Raspberry Pi
Sense Hat. Most of the code used for getting the acurate room temperature is
found at the following URL.
http://yaab-arduino.blogspot.com/2016/08/accurate-temperature-reading-sensehat.html
'''
import os
import time

from sense_hat import SenseHat

sense = SenseHat()

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
	
def getSmoothTemperature(temp, timeLength):

    print('Smoothing out temperatures..')

	# get the average of fluctuating temperatures
    secs = 0
    while secs < timeLength:
        temp = get_smooth(temp) 
        time.sleep(1)
        secs +=1

    return temp

# use moving average to smooth readings
def get_smooth(x):

	if not hasattr(get_smooth, "t"):
		get_smooth.t = [x,x,x]

	get_smooth.t[2] = get_smooth.t[1]
	get_smooth.t[1] = get_smooth.t[0]
	get_smooth.t[0] = x
	xs = (get_smooth.t[0]+get_smooth.t[1]+get_smooth.t[2])/3

	return(xs)
	
def getHumidity():
	return sense.get_humidity()

def getAcceleration():
    return sense.get_accelerometer_raw()

def getOrientation():
    return sense.get_orientation()