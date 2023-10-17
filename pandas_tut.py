#%%
# https://github.com/ourcodingclub/CC-python-pandas-matplotlib
# https://ourcodingclub.github.io/tutorials/pandas-python-intro/
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
