import pandas as pd
import numpy as np


# Column selection
print("\n Column Selection")
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d,dtype=np.int64)
df = df.fillna(0)
#df = pd.DataFrame(df, dtype=np.int64)
df['one'] = df['one'].astype(int)
print (df ['one'])

# Add a new Column in DF
print("\n Add a new Column in DF")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print (df)

# Adding a new column using the existing columns in DataFrame:
print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']
print(df)

# Deleting Columns using del
del df['four']

# Delete using a pop function
df.pop('three')
print(df)

# Row Transformations

# Selecting a row
print("\n Selecting a row")
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d,dtype=np.int64)

print(df.loc['a'])

# Selecting using numeric index
print (df.iloc[0])

# Adding a row
print("\n Adding a row")
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d,dtype=np.int64)
df2 = pd.DataFrame({'one' : pd.Series([3, 5, 7], index=['a', 'b', 'c']),
   'two' : pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])})
df = df.append(df2)
print(df)

# Deleting a row
print("\n Deleting a row")
df = df.drop('d')
print(df)
