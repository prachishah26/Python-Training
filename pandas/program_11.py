# Write a Pandas program to create today's date

import pandas as pd
import numpy as np
data = pd.read_csv("ufo.csv")
generate_todays_date = pd.to_datetime('today').date()
print(generate_todays_date)