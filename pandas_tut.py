#%%
# https://github.com/ourcodingclub/CC-python-pandas-matplotlib
# https://ourcodingclub.github.io/tutorials/pandas-python-intro/
# https://pandas.pydata.org/docs/reference/api/pandas.Series.html
# https://pandas.pydata.org/docs/user_guide/dsintro.html#basics-series

import pandas as pd
#%%
scottish_hills = {'Hill Name': ['Ben Nevis', 'Ben Macdui', 'Braeriach', 'Cairn Toul', 'Sgòr an Lochain Uaine'],
                  'Height': [1345, 1309, 1296, 1291, 1258],
                  'Latitude': [56.79685, 57.070453, 57.078628, 57.054611, 57.057999],
                  'Longitude': [-5.003508, -3.668262, -3.728024, -3.71042, -3.725416]}
scottish_hills
# %%
dataframe = pd.DataFrame(scottish_hills)
dataframe
# %%
dataframe = pd.DataFrame(scottish_hills, columns=['Longitude', 'Hill Name', 'Height', 'Latitude'])
dataframe
# %%
print(dataframe.head(3))
# %%
print(dataframe.tail(2))
# %%
print(dataframe['Hill Name'])
# %%
print(dataframe['Height'])
# %%
# accesing first raw in a different way:
# iloc is short for “integer location
dataframe.iloc[0]
# %%
dataframe.iloc[0,0]
# %%
dataframe['Hill Name'][0]
# %%
#An even quicker way to access our columns (less typing) is to treat the names as if they were attributes of our DataFrame, like this:
dataframe.Height
# %%
dataframe.Height[0]
# %%
dataframe.Height > 1300
# %%
type(dataframe.Height > 1300)
# %%
# proper filtration of data:
dataframe[dataframe.Height > 1300]
# %%
dataframe
# %%
dataframe['Region'] = ['Grampian', 'Cairngorm', 'Cairngorm', 'Cairngorm', 'Cairngorm']
# %%
dataframe
# %%
scot_hills = pd.read_csv("scottish_hills.csv")
print(scot_hills.head(10))
# %%
scot_hills.head(10)
# %%
small = scot_hills.head(3)
small
# %%
sorted_hills = scot_hills.sort_values(by=['Height'], ascending=False)
sorted_hills.head(1)
# %%
sorted_hills.Height[:3]
# %%
sorted_hills.iloc[:3]
# %%
type(sorted_hills.iloc[:3, -1])
# %%
list_ = [[1,2], [3,4]]
# %%
list_[:][1]
# %%
import matplotlib.pyplot as plt
x = scot_hills.Height
y = scot_hills.Latitude
plt.scatter(x, y)
plt.show()
# %%
# Below are the quick examples
# Example 1: Split the DataFrame using iloc[] by rows
df1 = scot_hills.iloc[:2, :]
df2 = scot_hills.iloc[2:, :]
df1

# %%
df2
# %%
# Example 2: Split the DataFrame using iloc[] by columns
df1 = scot_hills.iloc[:,:2]
df2 = scot_hills.iloc[:,2:]

# %%
df1
# %%
# Example 3: Split Dataframe using groupby() &
# Grouping by particular dataframe column
grouped = scot_hills.groupby(scot_hills['Hill Name'])
df1 = grouped.get_group("The Saddle")
# %%
df1
# %%
# Example 4: split DataFrame using sample()
df1 = scot_hills.sample(frac = 0.01, random_state = 200)
df1
# %%
df1 = scot_hills.iloc[:2, :]
df2 = scot_hills.iloc[2:, :]
df1
# %%
frames = [df1, df2]
result = pd.concat(frames)
result
# %%
In [1]: df1 = pd.DataFrame(
   ...:     {
   ...:         "A": ["A0", "A1", "A2", "A3"],
   ...:         "B": ["B0", "B1", "B2", "B3"],
   ...:         "C": ["C0", "C1", "C2", "C3"],
   ...:         "D": ["D0", "D1", "D2", "D3"],
   ...:     },
   ...:     index=[0, 1, 2, 3],
   ...: )
   ...: 

In [2]: df2 = pd.DataFrame(
   ...:     {
   ...:         "A": ["A4", "A5", "A6", "A7"],
   ...:         "B": ["B4", "B5", "B6", "B7"],
   ...:         "C": ["C4", "C5", "C6", "C7"],
   ...:         "D": ["D4", "D5", "D6", "D7"],
   ...:     },
   ...:     index=[4, 5, 6, 7],
   ...: )
   ...: 

In [3]: df3 = pd.DataFrame(
   ...:     {
   ...:         "A": ["A8", "A9", "A10", "A11"],
   ...:         "B": ["B8", "B9", "B10", "B11"],
   ...:         "C": ["C8", "C9", "C10", "C11"],
   ...:         "D": ["D8", "D9", "D10", "D11"],
   ...:     },
   ...:     index=[8, 9, 10, 11],
   ...: )
   ...: 

In [4]: frames = [df1, df2, df3]

In [5]: result = pd.concat(frames)
result
# %%
result = pd.concat(frames, keys=["x", "y", "z"])
result
# %%
d = {'a': 1, 'b': 2, 'c': 3}
ser = pd.Series(data=d)
ser
# %%
# If data is dict-like and index is None, then the keys in the data are used as the index. 
# If the index is not None, the resulting Series is reindexed with the index values.
ser = pd.Series(data=d, index=['x', 'y', 'z'])
ser
# %%
# pp = {
#     'a' : 'one',
#     'b' : 'two',
#     'c' : 'three'
#     }
pp = ('one', 'two', 'three')
series_pio = pd.Series(data=pp)
series_pio
# %%
#The result of an operation between unaligned Series will have the union of the indexes involved. 
# If a label is not found in one Series or the other, the result will be marked as missing NaN. 
# Being able to write code without doing any explicit data alignment grants immense 
# freedom and flexibility in interactive data analysis and research. 
# The integrated data alignment features of the pandas data structures set pandas 
# apart from the majority of related tools for working with labeled data.
ooo = series_pio.iloc[1:] + series_pio.iloc[:-1]
ooo
# %%
# https://stackoverflow.com/questions/38256104/differences-between-merge-and-concat-in-pandas
# https://studymachinelearning.com/difference-between-merge-join-and-concatenate/

data1 = {'key1':['k0','k1'], 'name' :['mark','juli'],'city':['New York','Paris']}
data2 = {'key1':['k1','k2'],'name' :['john','alex'],'city':['London','Tokyo']}

df1 = pd.DataFrame(data1,index = [0,1],columns=['key1','city','name'])
df2 = pd.DataFrame(data2,index=[1,'k0'],columns=['key1','city','name'])

df1
# %%
df2
# %%
df1.merge(df2,on="key1")  # by default this is INNER JOIN (AND logic operator)
# %%
# https://pandas.pydata.org/docs/reference/api/pandas.merge.html#pandas.merge
df1.merge(df2,on="key1",how='outer')
# %%
df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [1, 2, 3, 5]})
df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [5, 6, 7, 8]})
# %%
df1
# %%
df2
# %%
df1.merge(df2)
# %%
df1.merge(df2, left_on='lkey', right_on='rkey',
          suffixes=('_left', '_right'))
# %%
df1 = pd.DataFrame({'a': ['foo', 'bar'], 'b': [1, 2]})
df2 = pd.DataFrame({'a': ['foo', 'baz'], 'c': [3, 4]})
# %%
df1
# %%
df2
# %%
df1.merge(df2, how='inner')
# %%
df1.merge(df2, how='inner', on='a')
# %%
df1.merge(df2, how='cross')
# %%
