import sqlite3

connection = sqlite3.connect('data_log.db')

# display database data
def getTempAndHumid():
    
    cursor = connection.cursor()

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

    print('data read succesfully.')

    return table

# prints data from a table to the console
def printTable(table, headerString):
    print(headerString)

    for row in range(len(table)):
        print('| {0} |   {1}   | {2} |'.format(
            table[row][0], table[row][1], table[row][2]))

    print('|----------------------------------------------------|')

def main():
    # read temperature and humidty from database
    temperatureTable = getTempAndHumid()

    temp_humid_header = 'Temperature and humidty log\n'
    temp_humid_header += '|----------------------------------------------------|\n'
    temp_humid_header += '|      Date And Time       |  Temperature | Humidity |\n'
    temp_humid_header += '|----------------------------------------------------|'

    # print the temperature and humidity to the console
    printTable(temperatureTable, temp_humid_header)

    connection.close()

main()