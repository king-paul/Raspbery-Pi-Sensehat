CREATE DATABASE data_log;

CREATE TABLE data_log.temp_and_humid (
 date_time datetime PRIMARY KEY,
 temperature float,
 humidity float
);

CREATE TABLE data_log.accel_and_orient (
 date_time datetime PRIMARY KEY,
 x int,
 y int,
 z int,
 pitch int,
 roll int,
 yaw int
);