# Programming the Internet Of Things - Assignment 1
The first assignment for the course "Programming the internet of things" which us done using the Rasberry Pi and seneshat.

## Starting the crontab
If you have crontab set up add the following to crontab-e: * * * * * /home/pi/python/assignment1/log_sense_data.py

This will set the cronjob up to run every minute. To change the interval, e.g. 30mins type the following:
*/30 * * * * /home/pi/python/assignment1/log_sense_data.py

Once this is done you can start the cron job by typing 'sudo /etc/init.d/cron start'

## Logging sensehat data to the database
If you want to log data manually without using a cronjob you can do so by typing './log_sense_data.py'

## Starting the webserver
type 'sudo ./webserver.py' to start the webserver and copy the IP address it displays into your web browser address bar to view information from the database.

## Sending notifications to pushbullet
To do this run the push notification python program by typing './push_notify.py'

## Greet and log nearby Bluetooth devices
This can be done by running the bluetooth greeting python program by typing './bluetooth_greeting.py'
