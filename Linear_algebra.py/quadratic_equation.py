
import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.DataFrame({"x":range(-5,6)})
dataframe["y"] = -2*dataframe["x"]**2 + 5*dataframe["x"]+ 10
print(dataframe)
plt.plot(dataframe.x,dataframe.y,color="cyan")
plt.grid()
plt.show()

