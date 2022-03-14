# Sort all cars by Price column

import pandas as pd
import numpy as np

data = pd.read_csv("Automobile_data.csv")
data = data.replace("?",np.nan)
data = data.fillna(np.nan)

data['price'] = pd.to_numeric(data['price'])
# print(data)

data = data.sort_values(by=['price'],ascending = False)
print(data)
