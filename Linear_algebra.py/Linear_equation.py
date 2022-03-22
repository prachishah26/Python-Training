import pandas as pd
import matplotlib.pyplot as plt

#equation1 : y = (3x-4)/2
#equation2 : y = -(3x-4)/2
dataframe = pd.DataFrame({'x':range(-10,11)})
dataframe['y'] = (3*dataframe['x']-4)/2

dataframe2 = pd.DataFrame({'x':range(-10,11)})
dataframe2['y'] = -(3*dataframe['x']-4)/2


print(dataframe)
fig,axs = plt.subplots(2)
fig.suptitle("Linear equations")

axs[0].plot(dataframe.x,dataframe.y,color = "magenta")
axs[1].plot(dataframe2.x,dataframe2.y)
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.show()