# Write a Python program to extract year, month, date and time using Lambda.

# 2020-01-15 09:03:32.744178
#  2020
#  1
#  15
#  09:03:32.744178

from datetime import datetime
date_time = datetime.now()
year = lambda x : x.year
month = lambda x : x.month
day = lambda x : x.day
time = lambda x : x.strftime("%H:%M:%S.%f")
print(date_time)
print(year(date_time))
print(month(date_time))
print(day(date_time))
print(time(date_time))