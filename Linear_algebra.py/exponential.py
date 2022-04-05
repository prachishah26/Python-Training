import pandas as pd

# Create a dataframe with an x column containing values from -10 to 10
dataframe = pd.DataFrame ({'x': range(-5, 6)})

# Add a y column by applying the slope-intercept equation to x
dataframe['y'] = 2.0**dataframe['x']

#Display the dataframe
print(dataframe)

# Plot the line

from matplotlib import pyplot as plt

plt.plot(dataframe.x, dataframe.y, color="magenta")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline()
plt.axvline()
plt.show()