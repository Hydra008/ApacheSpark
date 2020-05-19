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

