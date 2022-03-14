# Write a Pandas program to calculate all the sighting days of the unidentified flying object (ufo) from the current date.

# import pandas as pd

# data = pd.read_csv(r"ufo.csv")


# data['Date_time'] = data['Date_time'].astype('datetime64[ns]')
# now = pd.to_datetime('today')
# print("Original Dataframe:")
# print(data.head())
# print("\nCurrent date:")
# print(now)


import pandas as pd
df = pd.read_csv('ufo.csv')
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')
print("Original Dataframe:")
print(df.head())
print("\nCurrent date of Ufo dataset:")
print(df.Date_time.max())
print("\nOldest date of Ufo dataset:")
print(df.Date_time.min())
print("\nNumber of days between Current date and oldest date of Ufo dataset:")
print((df.Date_time.max() - df.Date_time.min()).days)
