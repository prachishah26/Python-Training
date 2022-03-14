# From the given data set print the first and last five rows

import pandas as pd

data = pd.read_csv("Automobile_data.csv")

print(data.head())  #top five raws
print(data.tail())  #bottom five raws