# Write a Pandas program to calculate all the sighting days of the unidentified flying object (ufo) from the current date.

import pandas as pd

from datetime import datetime
df = pd.read_csv('ufo.csv')



df['Date_time'] = df['Date_time'].str.replace("24:00","00:00")
df['Date_time'] = pd.to_datetime(df['Date_time'])
print("top raws of Original Dataframe:")
print(df.head())
print("\nlast date of Ufo dataset:")
print(df.Date_time.max())
print("\nfirst date of Ufo dataset:")
print(df.Date_time.min())

# ------------------from input from user-------------------

date = pd.to_datetime(input('Input date in yyyy-mm-dd format'))
total_days_between_ufo_seen = df[df['Date_time']>date]
print(total_days_between_ufo_seen)
print("Days are : ",total_days_between_ufo_seen.Date_time.count())
