#!/usr/bin/env python3
from datetime import date
start_year = 1901
end_year = 2000
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
SUNDAY = 6

# solution 1
def isLeapYear(year):
	return bool(not year % 4 and (year % 100 or not year % 400))
def numDays(year, month):
	if month == 1 and isLeapYear(year):
		return 29
	return days_in_month[month]
first_day = 0 + 365 % 7
num_sundays = 0
for year in range(start_year, end_year+1):
	for month in range(12):
		if first_day == SUNDAY:
			num_sundays += 1
		first_day = (first_day + numDays(year, month)) % 7
print(num_sundays)

# solution 2
num_sundays = 0
for year in range(start_year, end_year+1):
	for month in range(12):
		if date(year, month+1, 1).weekday() == SUNDAY:
			num_sundays += 1
print(num_sundays)
