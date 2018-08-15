import requests
import json
import os

# import python file
from log_temp_humid import getTemperature

# This is the pushbullet access token from thepushbullet account
ACCESS_TOKEN = "o.l0fe3RaTNECme1QAnC1P3ELAuk65Ibyg"

def sendNotification(title, message):

    json_data = {"type": "note", "title": title, "body": message}
    
    response = requests.post('https://api.pushbullet.com/v2/pushes', 
                        data=json.dumps(json_data),
                        headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 
                        'Content-Type': 'application/json'})

    # check if push notification was successful
    if response.status_code == 200:
        print('Notification sent to Pushbullet')
    else:
        print('Error sending notification. Status code: {}'
        .format(response.status_code))

def main():
    # get the ip address
    ip_address = os.popen('hostname -I').read()

    # get the temperature
    temperature = getTemperature()

    # create the message
    message = 'The temperature is %.2f°C\n' % temperature
    if temperature < 20:
        message += 'Dont forget to bring a sweater!\n'

    # send the norification
    sendNotification('From Raspberry Pi:', message)

# start the script
main()