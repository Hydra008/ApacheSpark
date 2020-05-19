import pandas as pd
import numpy as np

def adder(ele1,ele2):
   return ele1+ele2

# Transforming entire dataFrame
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
print(df)
print('Applying transformation using pipe function')
df = df.pipe(adder,10)
print(df)

# Transforming a row or column
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
print(df)
print('Applying transformation on columnwise')
df = df.apply(lambda x: x + 5)
print(df)

# applying transformation on row
df = df.iloc[1].map(lambda x: x*5 / 2)
print(df)

df1 = pd.DataFrame(np.random.rand(5,3), columns=['col1','col2','col3'])
print(df1)

# Map only iterates over Series (1D)
print(df1['col1'].map(lambda x: x*20))

# Apply allows you to apply a function on multiple rows/columns or the entire DF
print(df1.iloc[[0,2]].apply(lambda x: x*20))

# ApplyMap needs all columns to be of numeric type
print(df1.applymap(lambda x: x*50))