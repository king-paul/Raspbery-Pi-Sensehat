''' createDB.py
This file is used to Create the tables in the SQLite database once data_log.db
has been created. It can also be used to delete any existing data in tables.
'''
# package needed for sql
import sqlite3 as sqlite

# databse file
dbFile = '/home/pi/python/assignment1/data_log.db'

# open the database
connection = sqlite.connect(dbFile)
cursor = connection.cursor()

with connection:
    # drop the tables if they already exist
    cursor.execute("DROP TABLE IF EXISTS temp_and_humid")
    cursor.execute("DROP TABLE IF EXISTS accel_and_orient")
    cursor.execute("DROP TABLE IF EXISTS bluetooth_devices")

    # create the temperature and humidity table
    cursor.execute("CREATE TABLE temp_and_humid (\n" +
                   "date_time datetime PRIMARY KEY,\n" +
                   "temperature NUMERIC,\n" +
                   "humidity NUMERIC)"
                   )

    # create the accelerometer and orientation table
    cursor.execute("CREATE TABLE accel_and_orient (\n" +
                   "date_time datetime PRIMARY KEY,\n" +
                   "x NUMERIC,\n" +
                   "y NUMERIC,\n" +
                   "z NUMERIC,\n" +
                   "pitch NUMERIC,\n" +
                   "roll NUMERIC,\n" +
                   "yaw NUMERIC)"
                    )

    # create table for found bluetooth devices
    cursor.execute("CREATE TABLE bluetooth_devices (\n" +
                  "date_time datetime PRIMARY KEY,\n" +
                  "mac_address TEXT,\n" +
                  "device_name TEXT)"
                  )

print('Database Schema created successfully.')