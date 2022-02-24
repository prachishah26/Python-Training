# Write a Python program to extract year, month, date and time using Lambda.

# 2020-01-15 09:03:32.744178
#  2020
#  1
#  15
#  09:03:32.744178

from datetime import datetime
d_t = datetime.now()
year = lambda x : x.year
month = lambda x : x.month
day = lambda x : x.day
time = lambda x : x.strftime("%H:%M:%S.%f")
print(d_t)
print(year(d_t))
print(month(d_t))
print(day(d_t))
print(time(d_t))