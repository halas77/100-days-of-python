import pandas as pd

df  = pd.read_csv('day-72/602 QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

# print(df.head())
# print(df.shape)
# print(df.count())

group = df.groupby('TAG').sum()


time = df['DATE']




print(time)