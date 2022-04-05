# import statsmodels.api as sm

# df = sm.datasets.get_rdataset('GaltonFamilies', package='HistData').data

# # Create a data frame of gender counts
# genderCounts = df['gender'].value_counts()


# from matplotlib import pyplot as plt
# genderCounts.plot(kind='pie', title='Gender Counts', figsize=(6,6))
# plt.legend()
# plt.show()


# from statistics import mean
# import random
# import matplotlib.pyplot as plt
# height = [4.5, 4.6, 4.7, 4.8, 4.9, 5, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6, 6.1, 6.2, 6.3, 6.4, 6.5, 4.5, 4.6, 4.7, 4.8, 4.9, 5, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6, 6.1, 6.2, 6.3, 6.4, 6.5]
# x = range(1,43)
# plt.plot(x,height,color = "red")
# height_sample1 = random.choices(height, k = 10)
# height_sample2 = random.choices(height, k = 12)
# height_sample3 = random.choices(height, k = 15)
# height_sample4 = random.choices(height, k = 19)

# print("mean of population",mean(height))
# print("sample1",mean(height_sample1))
# print("sample2",mean(height_sample2))
# print("sample3",mean(height_sample3))
# print("sample4",mean(height_sample4))
# plt.show()


t = True
print(int(t))