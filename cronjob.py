#!/usr/bin/env python3
from crontab import CronTab

# initialize cron
cron = CronTab(user = 'pi')
cron.remove_all()

# create a new cron job
job = cron.new(command='/home/pi/python/assignment1/log_temp_humid.py')

job.minute.every(1) # configure job to run once a minute
cron.write() # start the cron job

print('Temperature and Humidity logging cron job started.')
