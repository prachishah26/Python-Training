# Clean data and update the CSV file (Replace all column values which contain ‘?’ and n.a with NaN.)

import pandas as pd
import numpy as np
data = pd.read_csv("Automobile_data.csv")
print(data.info())

data = data.replace("?",np.nan)
# data = data.replace("n.a",np.nan)
data = data.fillna(np.nan)
print(data.sample(5))
print(data.info())