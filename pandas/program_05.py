# Count total car per company
import pandas as pd
import numpy as np

data = pd.read_csv("Automobile_data.csv")

car_counts = data["make"].value_counts()
print(car_counts)