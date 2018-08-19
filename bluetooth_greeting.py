
import bluetooth
import os
from sense_hat import SenseHat

from log_sense_data import getTemperature

sensehat = SenseHat() # create sense hat object

temperature = getTemperature() # get the temperature

print('Searching for nearby devices...')

# From Shekar Kalra's week05 lecture material
nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("found %d devices" % len(nearby_devices))

# lists all the nearby deivces and greets each one
for addr, name in nearby_devices:
    print("%s %s" % (addr, name))

    sensehat.show_message("Hello there %s!" % (name), scroll_speed=0.05)
    sensehat.show_message("the temperature is %.2f" % (temperature),
    text_colour=(0, 255, 0), scroll_speed=0.05)