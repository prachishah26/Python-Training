# Find each company’s Highest price car

import pandas as pd
import numpy as np
data = pd.read_csv("Automobile_data.csv")
data = data.replace("?",np.nan)
data = data.fillna(np.nan)
data['price'] = pd.to_numeric(data['price'])
car = data.groupby('make')['price'].max()
# price = car['make','price'].max()
print(car)


# max_price = data['price'].astype(float).max()
# print(np.unique(data[data['price'] == max_price]['make']))
