# Find the average mileage of each car making company

import pandas as pd
import numpy as np
data = pd.read_csv("Automobile_data.csv")

car = data.groupby('make')
avg_mileage = car['make','highway-mpg'].mean()
print(avg_mileage)