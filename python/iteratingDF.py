import pandas as pd
import numpy as np

N = 20
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])

print (df)
# iterating over columns
print('iterating over columns')
for key,value in df.iteritems():
   print (key)
   print(value)

# iterate over rows
print('iterating over rows')
for row_index, row in df.iterrows():
    print(row_index)
    print(row)


