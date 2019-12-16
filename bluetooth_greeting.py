#!/usr/bin/env python3
import bluetooth
import os
import sqlite3
from sense_hat import SenseHat

from sensehat_data import getTemperature

sensehat = SenseHat() # create sense hat object

temperature = getTemperature() # get the temperature

# scans for nearby bluetooth devices and returns them
def findDevices():
    print('Searching for nearby devices...')

    # From Shekar Kalra's week05 lecture material
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("found %d devices" % len(nearby_devices))

    return nearby_devices

# logs the found details into the sqlite database
def logFoundDevices(nearby_devices):
    connection = sqlite3.connect('data_log.db')
    cursor = connection.cursor()

    # add each row to the table
    for addr, name in nearby_devices:
        cursor.execute("INSERT INTO bluetooth_devices VALUES(" +
                       "DATETIME('now'), (?), (?))", (""+addr, ""+name))
    
    # commit and close database
    connection.commit()
    connection.close()

    print('Nearby devices saved to database')

# lists all the nearby deivces and greets each one
def greetDevices(nearby_devices):

    # From Shekar Kalra's week05 lecture material
    for addr, name in nearby_devices:
        print("%s %s" % (addr, name))

        sensehat.show_message("Hello there %s!" % (name), scroll_speed=0.05)
        sensehat.show_message("the temperature is %.2f" % (temperature),
        text_colour=(0, 255, 0), scroll_speed=0.05)

def main():
    deivces = findDevices()
    logFoundDevices(deivces)
    greetDevices(deivces)

main() # starts the program