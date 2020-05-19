import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print (df)
print(df.isnull())

# Handling missing values
print('filling missing values with 0')
df1 = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
df1 = df1.fillna(0)
print(df1)


print('filling missing values with backfill')
df3 = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
df3 = df3.fillna(method='backfill')
print(df3)

print('dropping missing values')
print(df.dropna())

