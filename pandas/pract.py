
import pandas as pd
import numpy as np


# # Creating empty series
# ser = pd.Series()

# print(ser)

# # simple array
# data = np.array(['g', 'e', 'e', 'k', 's'])

# ser = pd.Series(data)
# print(ser)



# # Calling DataFrame constructor
# df = pd.DataFrame()
# print(df)

# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is',
			'portal', 'for', 'Geeks']
# data = {"a":"prachi", "b":"shah"}
# # Calling DataFrame constructor on list
# df = pd.DataFrame(data,index = ["b","a"])
# print(df)



# data = {'a' : 0., 'b' : 1., 'c' : 2.}
# s = pd.Series(data,index=['b','c','d','a'])
# print(s)

# s = pd.Series(5,index = [0,1,2,3,4,5,6,7,8,9,10])
# print(s[0])
# print(s[:3])


# s = pd.Series(data = [0,1,2,3], index = ['a','b','c','d'])
# print(s['a'])

# d = [1,2,3,4,5]
# s = pd.DataFrame(d)
# print(s)

# data = [["prachi",22],["shah",22],["rachu",18]]
# df = pd.DataFrame(data,columns=["name","age"])
# print(df)


# import pandas as pd
# data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
# df = pd.DataFrame(data)
# print(df)

# data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
# df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
# print(df)

# data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
# df = pd.DataFrame(data)
# print(df)

# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

# df = pd.DataFrame(d)
# print(df['two'])

# df['three']=pd.Series([10,20,30],index=['a','b','c'])
# print(df)

# print ("Adding a new column using the existing columns in DataFrame:")
# df['four']=df['one']+df['three']
# print(df)

# del df['one']
# print(df)

# # using pop function
# print ("Deleting another column using POP function:")
# df.pop('two')
# print(df)

# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
#    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

# df = pd.DataFrame(d)
# print(df.iloc[2])
# print(df.loc["b"])
# df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
# df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

# df = df.append(df2)
# print(df)

# df1 = df.drop(0)
# print(df1)

# df = pd.DataFrame(np.random.randn(4))
# print(df.T)

#Create a Dictionary of series
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
#    'Lee','David','Gasper','Betina','Andres']),
#    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
# }

# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df.mean())

# df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
# df.apply(np.mean)
# print(df.apply(np.mean))

# df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])

# My custom function
# df['col1'].map(lambda x:x*100)
# print(df.apply(np.mean))

# print(np.random.randn(10,3))


# N=20
# df = pd.DataFrame({
#    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
#    'x': np.linspace(0,stop=N-1,num=N),
#    'y': np.random.rand(N),
#    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
#    'D': np.random.normal(100, 10, size=(N)).tolist()
#    })

# print(df)

# for col in df:
#    print(col)

# df = pd.DataFrame(np.random.randn(10, 4),
#    index = pd.date_range('1/1/2000', periods=10),
#    columns = ['A', 'B', 'C', 'D'])
# print(df)


# df = pd.read_csv('/home/woc/Downloads/data.csv')
# # pd.options.display.max_rows = 9
# print(df.describe()) 

# new_df = df.fillna(7)
# print(new_df)

from datetime import datetime
df = pd.read_csv('ufo.csv')



df['Date_time'] = df['Date_time'].str.replace("24:00","00:00")

# df['Date_time'] = df['Date_time'].replace(df['Date_time'][10:],"")
# df['Date_time'] = datetime.strptime(df['Date_time'], '%d/%m/%y %I:%M')
# df['Date_time'] = pd.to_datetime(df['Date_time']).

df['Date_time'] = pd.to_datetime(df['Date_time'])
print("top raws of Original Dataframe:")
print(df.head())
print("\nlast date of Ufo dataset:")
print(df.Date_time.max())
print("\nfirst date of Ufo dataset:")
print(df.Date_time.min())

# ------------------from input from user-------------------

date = pd.to_datetime(input('Input date in yyyy-mm-dd format'))
total_days_between_ufo_seen = df[df['Date_time']>date]
print("Days are : ",total_days_between_ufo_seen.Date_time.count())

# print(date)