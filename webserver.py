#!/usr/bin/env python3
import os
from flask import Flask, render_template
import json

# external scripts
from read_database import getTempAndHumid, getAccelAndOrient

app = Flask(__name__)

# main route 
@app.route("/")
def index():	
	temp_humid_data = getTempAndHumid()
	accel_orient_data = getAccelAndOrient()
	
	return render_template('index.html',  tempTable = temp_humid_data,
	accelTable = accel_orient_data)

# starts the web server
if __name__ == "__main__":	
	host = os.popen('hostname -I').read()
	app.run(host='10.0.0.58', port=80, debug=False)
