import pandas as pd
import numpy as np

unsorted_df=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=['col2','col1'])
print (unsorted_df)

# using sort.index () which sorts by row labels in ascending by default
print('using sort.index () which sorts by row labels in ascending by default')
print(unsorted_df.sort_index())

# sorting in descending order
print('sorting in descending order')
print(unsorted_df.sort_index(ascending=False))
df = unsorted_df.sort_index(ascending=False)

# Sorting on column label
print('Sorting on column label')
print(unsorted_df.sort_index(axis=1))

# Sorting by values
print('Sorting by values which defaults to column name')

unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
print(unsorted_df)
sorted_df = unsorted_df.sort_values(by='col1')

print (sorted_df)
print('Sorting on values of multiple columns')
sorted_df = unsorted_df.sort_values(by=['col1','col2'])
print(sorted_df)