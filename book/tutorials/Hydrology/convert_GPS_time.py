#!/usr/bin/env python
u"""
convert_GPS_time.py (10/2017)
Return the calendar date and time for given GPS time.
Based on Tiffany Summerscales's PHP conversion algorithm
	https://www.andrews.edu/~tzs/timeconv/timealgorithm.html

INPUTS:
	GPS_Time: GPS time (standard = seconds since January 6, 1980 at 00:00)

OUTPUTS:
	month: Number of the desired month (1 = January, ..., 12 = December).
	day: Number of day of the month.
	year: Number of the desired year.
	hour: hour of the day
	minute: minute of the hour
	second: second (and fractions of a second) of the minute.

OPTIONS:
	OFFSET: number of seconds to offset each GPS time

PYTHON DEPENDENCIES:
	numpy: Scientific Computing Tools For Python (http://www.numpy.org)

PROGRAM DEPENDENCIES:
	convert_julian.py: convert Julian dates into calendar dates

UPDATE HISTORY:
	Updated 10/2017: added leap second from midnight 2016-12-31
	Written 04/2016
"""
import numpy as np
from convert_julian import convert_julian
import pdb

#-- PURPOSE: Define GPS leap seconds
def get_leaps():
	leaps = [46828800, 78364801, 109900802, 173059203, 252028804, 315187205,
		346723206, 393984007, 425520008, 457056009, 504489610, 551750411,
		599184012, 820108813, 914803214, 1025136015, 1119744016, 1167264017]
	return leaps

#-- PURPOSE: Test to see if any GPS seconds are leap seconds
def is_leap(GPS_Time):
	leaps = get_leaps()
	Flag = np.zeros_like(GPS_Time, dtype=np.bool)
	for leap in leaps:
		count = np.count_nonzero(np.floor(GPS_Time) == leap)
		if (count > 0):
			indices, = np.nonzero(np.floor(GPS_Time) == leap)
			Flag[indices] = True
	return Flag

#-- PURPOSE: Count number of leap seconds that have passed for each GPS time
def count_leaps(GPS_Time):
	leaps = get_leaps()
	#-- number of leap seconds prior to GPS_Time
	n_leaps = np.zeros_like(GPS_Time, dtype=np.uint)
	for i,leap in enumerate(leaps):
		count = np.count_nonzero(GPS_Time >= leap)
		if (count > 0):
			indices, = np.nonzero(GPS_Time >= leap)
			# print(indices)
			# pdb.set_trace()
			n_leaps[indices] += 1
	return n_leaps

#-- PURPOSE: Convert UNIX Time to GPS Time
def convert_UNIX_to_GPS(UNIX_Time):
	#-- calculate offsets for UNIX times that occur during leap seconds
	offset = np.zeros_like(UNIX_Time)
	count = np.count_nonzero((UNIX_Time % 1) != 0)
	if (count > 0):
		indices, = np.nonzero((UNIX_Time % 1) != 0)
		UNIX_Time[indices] -= 0.5
		offset[indices] = 1.0
	#-- convert UNIX_Time to GPS without taking into account leap seconds
	#-- (UNIX epoch: Jan 1, 1970 00:00:00, GPS epoch: Jan 6, 1980 00:00:00)
	GPS_Time = UNIX_Time - 315964800
	leaps = get_leaps()
	#-- calculate number of leap seconds prior to GPS_Time
	n_leaps = np.zeros_like(GPS_Time, dtype=np.uint)
	for i,leap in enumerate(leaps):
		count = np.count_nonzero(GPS_Time >= (leap - i))
		if (count > 0):
			indices, = np.nonzero(GPS_Time >= (leap - i))
			n_leaps[indices] += 1
	#-- take into account leap seconds and offsets
	GPS_Time += n_leaps + offset
	return GPS_Time

#-- PURPOSE: Convert GPS Time to UNIX Time
def convert_GPS_to_UNIX(GPS_Time):
	#-- convert GPS_Time to UNIX without taking into account leap seconds
	#-- (UNIX epoch: Jan 1, 1970 00:00:00, GPS epoch: Jan 6, 1980 00:00:00)
	UNIX_Time = GPS_Time + 315964800
	#-- number of leap seconds prior to GPS_Time
	n_leaps = count_leaps(GPS_Time)
	UNIX_Time -= n_leaps
	#-- check if GPS Time is leap second
	Flag = is_leap(GPS_Time)
	if Flag.any():
		#-- for leap seconds: add a half second offset
		indices, = np.nonzero(Flag)
		UNIX_Time[indices] += 0.5
	return UNIX_Time

#-- PURPOSE: convert from GPS time to calendar dates
def convert_GPS_time(GPS_Time, OFFSET=0.0):
	#-- convert from standard GPS time to UNIX time accounting for leap seconds
	#-- and adding the specified offset to GPS_Time
	UNIX_Time = convert_GPS_to_UNIX(np.array(GPS_Time) + OFFSET)
	#-- calculate Julian date from UNIX time and convert into calendar dates
	#-- UNIX time: seconds from 1970-01-01 00:00:00 UTC
	julian_date = (UNIX_Time/86400.0) + 2440587.500000
	cal_date = convert_julian(julian_date)
	#-- include UNIX times in output
	cal_date['UNIX'] = UNIX_Time
	#-- return the calendar dates and UNIX time
	return cal_date
