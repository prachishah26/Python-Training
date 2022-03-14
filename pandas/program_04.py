# Print All Toyota Cars details

import pandas as pd
import numpy as np

data = pd.read_csv("Automobile_data.csv")
print(data[data["make"] == "toyota"])