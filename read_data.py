import sqlite3

connection = sqlite3.connect('data_log.db')
cursor = connection.cursor()

# display database data
def getTempAndHumid():
    
    # create empty 2d list
    table = []

    # retuen first column from table
    cursor.execute("SELECT datetime(date_time, 'localtime') FROM temp_and_humid")
    dateTimes = cursor.fetchall()

    # return second column from table
    cursor.execute("SELECT round(temperature, 2) FROM temp_and_humid")
    temps = cursor.fetchall()

    # return third colum from table
    cursor.execute("SELECT  round(humidity, 2) FROM temp_and_humid")
    humids = cursor.fetchall()

    # iterate through each list add them to the 2d table list
    for row in range(len(dateTimes)):
        table.append([]) # adds a new row to list
        table[row].append(dateTimes[row])
        table[row].append(temps[row])
        table[row].append(humids[row])

    print('read temperature and humidity')

    return table

def getAccelAndOrient():    
    # Date and time of logging
    cursor.execute("SELECT datetime(date_time, 'localtime') FROM accel_and_orient")
    dateTimes = cursor.fetchall()

    # X
    cursor.execute("SELECT round(x, 2) FROM accel_and_orient")
    x = cursor.fetchall()

    # Y
    cursor.execute("SELECT round(y, 2) FROM accel_and_orient")
    y = cursor.fetchall()

    # Z
    cursor.execute("SELECT round(z, 2) FROM accel_and_orient")
    z = cursor.fetchall()

    # Pitch
    cursor.execute("SELECT round(pitch, 2) FROM accel_and_orient")
    pitch = cursor.fetchall()

    # Roll
    cursor.execute("SELECT round(roll, 2) FROM accel_and_orient")
    roll = cursor.fetchall()

    # Yaw
    cursor.execute("SELECT round(yaw, 2) FROM accel_and_orient")
    yaw = cursor.fetchall()

    # create empty 2d list
    table = []

    # iterate through each list add them to the 2d table list
    for row in range(len(dateTimes)):
        table.append([]) # adds a new row to list
        table[row].append(dateTimes[row])
        table[row].append(x[row])
        table[row].append(y[row])
        table[row].append([row])
        table[row].append([row])
        table[row].append([row])
        table[row].append([row])

    return table

# prints data from a table to the console
def printTempAndHumidTable(table):
    print('Temperature and humidty log\n' +
          '|----------------------------------------------------|\n' +
          '|      Date And Time       |  Temperature | Humidity |\n' +
          '|----------------------------------------------------|')

    for row in range(len(table)):
        print('| {0} |   {1}   | {2} |'.format(
            table[row][0], table[row][1], table[row][2]))

    print('|----------------------------------------------------|\n')

def printAccelAndOrientTable(table):
    print('Acceleromater and Orientation log\n' +
          '|------------------------------------------------------------------------------|\n' +
          '|      Date And Time       |    x     |    y    |    z    | pitch | roll | yaw |\n' +
          '|------------------------------------------------------------------------------|'
    )

    for row in range(len(table)):
        print('| {0} | {1} | {2} |   {3}   |  {4}  |  {5} | {6} |'.format(
            table[row][0], table[row][1], table[row][2], table[row][3],
            table[row][4], table[row][5], table[row][6]))

    print('|------------------------------------------------------------------------------|\n')

def main():
    # read temperature and humidty from database
    temperatureTable = getTempAndHumid()
    accelerometerTable = getAccelAndOrient()

    # print the temperature and humidity to the console
    printTempAndHumidTable(temperatureTable)
    printAccelAndOrientTable(accelerometerTable)

    connection.close()

main()