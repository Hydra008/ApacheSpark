# Pandas

Pandas is a python library for data manipulation and data analysis
with the help of efficient data structures.

## Pandas Data Structures

Pandas deals with the following three data structures −

<li>Series</li>
<li>DataFrame</li>
<li>Panel</li>

### Pandas Series

<p>Series is a one-dimensional labeled array capable of holding data of 
any type (integer, string, float, python objects, etc.). The axis 
labels are collectively called index. </p>

<b>Syntax </b>
```
pandas.Series( data, index, dtype, copy)
```
A series can be created using various inputs like −
Array
Dict
Scalar value or constant

#### Creating a Pandas series

<b>Creating a series from array</b>

```
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print s

# output
0   a
1   b
2   c
3   d
dtype: object
```

<b>Creating a series from array using custom index</b>

```
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print s

# output
100  a
101  b
102  c
103  d
dtype: object
```

<b>Create a Series from dict</b>

```
import pandas as pd
import numpy as np
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print s

#output
a 0.0
b 1.0
c 2.0
dtype: float64
```

<b>Creating a list form scalar</b>

```
import pandas as pd
import numpy as np
s = pd.Series(5, index=[0, 1, 2, 3])
print s

#Output
0  5
1  5
2  5
3  5
dtype: int64
```

#### Accessing a pandas series

```
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

print s[0] # 'a'
print s[:3]
#
a  1
b  2
c  3
dtype: int64

`

<b>You can retrieve using index as well</b>
```
### Pandas Dataframe

<b>syntax</b>

```
pandas.DataFrame( data, index, columns, dtype, copy)
```

You can create a dataframe from list, dict or list of dicts or dicts of
lists and pandas series.

#### Creating a DataFrame

<b>Creating a dataframe from list</b>
```
data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data)

#output
   0
0  1
1  2
2  3
3  4
4  5
```

<b>Creating a dataframe from 2D list</b>
```
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print (df)

# output
     Name  Age
0    Alex   10
1     Bob   12
2  Clarke   13
```

<b>Creating a dataframe and changing types</b>

```
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print (df)

# output
Creating a dataframe and changing the datatype
     Name   Age
0    Alex  10.0
1     Bob  12.0
2  Clarke  13.0
```

<b>Creating a dataframe from Dict of Arrays/Lists</b>

```
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print (df)

# output
    Name  Age
0    Tom   28
1   Jack   34
2  Steve   29
3  Ricky   42
```

<b>Creating a dataframe from list of Dict</b>
```
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print (df)

# output
   a   b     c
0  1   2   NaN
1  5  10  20.0
```

#### Selecting, adding, deleting  Columns

<b>Selecting columns</b>

```
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d,dtype=np.int64)
print (df ['one'])

# Output
a    1
b    2
c    3
d    0
Name: one, dtype: int64
```

<b>Adding a column</b>
```
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print (df)

#output

   one  two  three
a    1    1   10.0
b    2    2   20.0
c    3    3   30.0
d    0    4    NaN
```

<b>Deleting a column</b>
```
del df['four']

# Difference between del and pop is that pop returns the deleted value
df.pop('three')
print(df)
```


#### Selecting, adding, deleting, Rows

<b>Selecting a row </b>
```
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d,dtype=np.int64)

print(df.loc['a'])
# or
print(df.iloc[0])

# output
one    1.0
two    1.0
Name: a, dtype: float64
```

<b>Adding a row</b>
```
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d,dtype=np.int64)
df2 = pd.DataFrame({'one' : pd.Series([3, 5, 7], index=['a', 'b', 'c']),
   'two' : pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])})
df = df.append(df2)
print(df)

# OUTPUT
 Adding a row
   one  two
a  1.0    1
b  2.0    2
c  3.0    3
d  NaN    4
a  3.0    9
b  5.0    8
c  7.0    7
d  NaN    6
```

<b>Deleting a row</b>

```
df = df.drop('d')

# Output
a  1.0    1
b  2.0    2
c  3.0    3
a  3.0    9
b  5.0    8
c  7.0    7
```


### Basic Operations

Here are some list of basic operations that can be done on DF

<li>axes: Returns a list of the row axis labels</li>
<li>ndim: Return dimension of data frame</li>
<li>size: Returns size of underlying data</li>
<li>head: return first n elements</li>
<li>tail: return last n elements</li>
<li>shape: returns shape of DF (rows and columns) </li>

```
import pandas as pd

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print (df)

# Return list of row axis labels
print("\n Return list of row axis labels")
print(df.axes)
# Return dimension of data frame
print("\n Return dimension of data frame")
print(df.ndim)

# Returns size of underlying data
print("\nReturns size of underlying data")
print(df.size)
# return first n elements
print("\nreturn first n elements")
print(df.head(2))
# return last n elements
print("\nreturn last n elements")
print(df.tail(2))
# returns shape of DF (rows and columns)
print("\nreturns shape of DF (rows and columns)")
print(df.shape)

# output
    Name  Age
0    Tom   28
1   Jack   34
2  Steve   29
3  Ricky   42

 Return list of row axis labels
[RangeIndex(start=0, stop=4, step=1), Index(['Name', 'Age'], dtype='object')]

 Return dimension of data frame
2

Returns size of underlying data
8

return first n elements
   Name  Age
0   Tom   28
1  Jack   34

return last n elements
    Name  Age
2  Steve   29
3  Ricky   42

returns shape of DF (rows and columns)
(4, 2)
```

### Statistics function

We can use various statistical function on dataframe as follows

<b>To run Statistical function on columns pass axis =1</b>

```
df.sum(1)
```

<b>Statistical methods that can be used</b>

<li>sum</li>
<li>mean</li>
<li>median</li>
<li>mode</li>
<li>std() - Standard deviation</li>
<li>min</li>
<li>max</li>
<li>abs() - absolute values</li>
<li>prod() - product of values</li>
<li>cumsum() - Cumulative Sum</li>
<li>cumprod() - Cumulative Product</li>
<li>describe(include='all') - gives all descriptive statistics</li>

### Applying functions on Dataframe

There are three ways to apply functions on dataframe
1. Apply on entire dataframe
2. Row or column wise application of function
3. Element wise application


#### Transforming entire dataframe using pipe()

```
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
print(df)
print('Applying transformation using pipe function')
df = df.pipe(adder,10)
print(df)

# output
       col1      col2      col3
0  1.718857  0.787601  2.037968
1 -0.944845 -1.139104  1.063389
2  0.961299 -1.173610  0.613398
3 -1.180832  0.199149  0.805835
4 -0.246160  0.581590  0.108767
Applying transformation using pipe function
        col1       col2       col3
0  11.718857  10.787601  12.037968
1   9.055155   8.860896  11.063389
2  10.961299   8.826390  10.613398
3   8.819168  10.199149  10.805835
4   9.753840  10.581590  10.108767
```

#### Transforming a row or column using apply()

```

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
print(df)
df = df.apply(lambda x:x +5)

# output
       col1      col2      col3
0 -0.117862 -0.630317  0.145441
1  0.007949  1.705826  0.408508
2  1.504659  0.088816  0.020661
3 -1.171822 -1.554522  0.296845
4  0.683876  0.503192  1.989633
Applying transformation on columnwise
       col1      col2      col3
0  4.882138  4.369683  5.145441
1  5.007949  6.705826  5.408508
2  6.504659  5.088816  5.020661
3  3.828178  3.445478  5.296845
4  5.683876  5.503192  6.989633
```

#### transforming elementwise transformation

```
# applying transformation on row
df = df.iloc[1].map(lambda x: x*5 / 2)
print(df)

# output
col1    12.519873
col2    16.764566
col3    13.521271
Name: 1, dtype: float64
```

### Reindexing 

```
import pandas as pd
import numpy as np

N=20

df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})

print(df)

#reindex the DataFrame
df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])
print(df_reindexed)

# Reindex dataframe to match other dataFrame
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])

df1 = df1.reindex_like(df2)
print (df1)

# Filling while reindexing
print ("Data Frame with Forward Fill:")
print (df2.reindex_like(df1,method='ffill'))

# Renaming
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print (df1)

print ("After renaming the rows and columns:")
print (df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},
index = {0 : 'apple', 1 : 'banana', 2 : 'durian'}))

# Output

            A     x         y       C           D
0  2016-01-01   0.0  0.795028  Medium   86.953740
1  2016-01-02   1.0  0.254945  Medium   94.182287
2  2016-01-03   2.0  0.898862    High   95.492506
3  2016-01-04   3.0  0.096036     Low   94.516071
4  2016-01-05   4.0  0.152021    High   82.622513
5  2016-01-06   5.0  0.037796    High   96.371575
6  2016-01-07   6.0  0.816849    High  115.329816
7  2016-01-08   7.0  0.380446  Medium  106.226126
8  2016-01-09   8.0  0.094131    High  102.506767
9  2016-01-10   9.0  0.076712     Low   89.613183
10 2016-01-11  10.0  0.571446     Low  117.415572
11 2016-01-12  11.0  0.939859    High   85.230536
12 2016-01-13  12.0  0.558896    High   89.593345
13 2016-01-14  13.0  0.599358    High   88.295449
14 2016-01-15  14.0  0.636190    High  106.802737
15 2016-01-16  15.0  0.259930     Low   97.237879
16 2016-01-17  16.0  0.831390  Medium   84.119010
17 2016-01-18  17.0  0.658593  Medium  105.334082
18 2016-01-19  18.0  0.278663  Medium  107.817295
19 2016-01-20  19.0  0.202887  Medium   76.769630
           A       C   B
0 2016-01-01  Medium NaN
2 2016-01-03    High NaN
5 2016-01-06    High NaN
       col1      col2      col3
0  1.491619  0.168158 -1.912189
1  1.306304 -0.829166 -0.769502
2 -0.112866 -0.543717 -1.594189
3 -0.104185 -0.199303  0.136900
4  1.147521  0.283549  0.919086
5 -0.833867 -1.605772  0.381373
6 -0.046821 -0.275396 -0.400615
Data Frame with Forward Fill:
       col1      col2      col3
0 -0.432203  1.321651  0.681611
1 -1.135024 -1.159128  0.015057
2  0.618168  1.106675 -0.334433
3  0.277927  0.083938 -0.989821
4  0.875348 -0.854404  0.497603
5 -1.997277 -1.352793 -0.210581
6  0.101080  0.701516  1.823472
       col1      col2      col3
0  0.681592  1.140943 -0.177661
1  0.294907 -0.073483  0.019141
2  2.492731  0.266581  0.850979
3 -0.034508 -0.494404 -0.828926
4  0.252649 -0.696356  0.248878
5 -1.971704 -0.109332 -0.709083
After renaming the rows and columns:
              c1        c2      col3
apple   0.681592  1.140943 -0.177661
banana  0.294907 -0.073483  0.019141
durian  2.492731  0.266581  0.850979
3      -0.034508 -0.494404 -0.828926
4       0.252649 -0.696356  0.248878
5      -1.971704 -0.109332 -0.709083
```

### Iterating over Dataframe

Iterating over a dataframe returns datatype based on the data structure
being used
1. Series - returns Value
2. Dataframe - returns column names
3. Panel - return item labels

#### To iterate over data frame

1. iteritems() − to iterate over the (key,value) pairs
2. iterrows() − iterate over the rows as (index,series) pairs
3. itertuples() − iterate over the rows as namedtuples

<b>iteritms - returns column name, col_series</b> 

```
import pandas as pd
import numpy as np

N = 20
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
print(df)

# Output
       col1      col2      col3
0  1.423772  1.369441 -1.853469
1  0.512531 -0.730716 -0.830438
2 -2.036453  0.848110  0.403173
3  0.715503  1.672805 -1.064612
col1
0    1.423772
1    0.512531
2   -2.036453
3    0.715503
Name: col1, dtype: float64
col2
0    1.369441
1   -0.730716
2    0.848110
3    1.672805
Name: col2, dtype: float64
col3
0   -1.853469
1   -0.830438
2    0.403173
3   -1.064612
Name: col3, dtype: float64
```
<b>iterrows - returns row index and row_series</b>

```
print('iterating over rows')
for row_index, row in df.iterrows():
    print(row_index)
    print(row)

#output
iterating over rows
0
col1    0.849058
col2    0.485207
col3   -1.820344
Name: 0, dtype: float64
1
col1    1.407456
col2    0.192189
col3    0.955135
Name: 1, dtype: float64
2
col1   -0.320405
col2    0.867971
col3    0.306524
Name: 2, dtype: float64
3
col1    0.359719
col2   -1.576341
col3    0.583396
Name: 3, dtype: float64
```

### Sorting a dataframe

There are 2 types of sorting available in pandas
1. By Label
2. By Value

<b> By Label </b>

```
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

# output
       col2      col1
1 -0.462110 -0.251198
4  0.175715  0.937223
6  0.655494  0.503132
2 -1.862162 -0.497150
3  1.788112  0.506676
5  1.510297  0.382907
9  0.203619  0.139120
8  0.605300 -0.014597
0 -0.437943  1.118221
7  1.789364 -1.761292
using sort.index () which sorts by row labels in ascending by default
       col2      col1
0 -0.437943  1.118221
1 -0.462110 -0.251198
2 -1.862162 -0.497150
3  1.788112  0.506676
4  0.175715  0.937223
5  1.510297  0.382907
6  0.655494  0.503132
7  1.789364 -1.761292
8  0.605300 -0.014597
9  0.203619  0.139120
sorting in descending order
       col2      col1
9  0.203619  0.139120
8  0.605300 -0.014597
7  1.789364 -1.761292
6  0.655494  0.503132
5  1.510297  0.382907
4  0.175715  0.937223
3  1.788112  0.506676
2 -1.862162 -0.497150
1 -0.462110 -0.251198
0 -0.437943  1.118221
Sorting on column label
       col1      col2
1 -0.251198 -0.462110
4  0.937223  0.175715
6  0.503132  0.655494
2 -0.497150 -1.862162
3  0.506676  1.788112
5  0.382907  1.510297
9  0.139120  0.203619
8 -0.014597  0.605300
0  1.118221 -0.437943
7 -1.761292  1.789364
```

<b>Sorting by values</b>

```
print('Sorting by values which defaults to column name')

unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
print(unsorted_df)
sorted_df = unsorted_df.sort_values(by='col1')

print (sorted_df)
print('Sorting on values of multiple columns')
sorted_df = unsorted_df.sort_values(by=['col1','col2'])
print(sorted_df)

# Output
   col1  col2
1     1     3
2     1     2
3     1     4
0     2     1
Sorting on values of multiple columns
   col1  col2
2     1     2
1     1     3
3     1     4
0     2     1
```

### Handling missing data

#### Check if is null

```

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print (df.isnull())

# output
     one    two  three
a  False  False  False
b   True   True   True
c  False  False  False
d   True   True   True
e  False  False  False
f  False  False  False
g   True   True   True
h  False  False  False

```

<b>while doing calculation on missing data, they are treated as 0.
But if all values are NaN then the result will be NaN
</b>

```
df.fillna(0)
df.fillna(method='pad')
df.fillna(method='backfill')
df.dropna()
```

<b>You can backfill, pad fill or drop missing values</b>

### Handling Categorical Data

You can create categorical data by following ways

1. Make an existing column dtype='categorical'
2. Using pd.Categorical()

<b>Make an existing column dtype='categorical'</b>

```
s = pd.Series(["a", "b", "c", "a"], dtype="category")
print(s)
```

<b>Using pd.Categories</b>
```
cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'],ordered=True)
print (cat)

# output
[a, b, c, a, b, c, NaN]
Categories (3, object): [c < b < a]
```

<b>Operations on list of Categories</b>

```
# Get Categories
print(dog.categories)

# rename Categories
s.cat.categories = ['Group 1','Group 2', 'Group 3']

# Add Categories
s = s.cat.add_categories([4])

# Delete Categories
s.cat.remove_categories("a")
```

### Handling text Data

Operations on text data includes
1. lower() - converts to lower case string
2. upper() - converts to upper case string
3. len() - length of String
4. split() - splits on the separator provided
5. replace(a,b) - replaces a with b
6. count() - returns count of apperances
6. islower(), isupper(), isnumeric()
7. strip() - removes white spaces
8. contains - checks for pattern provided
9. startswith(), endswith(), find() 

```
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print ("Strings that start with 'T':")
print s.str. startswith ('T')
```

### Window functions

Python provides 3 types of window function that can be applied to a 
dataframe

1. Rolling (uses same number of window each time)
2. Expanding (increasing number of window each time)
3. exponential moving average

```
df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print(df)
print (df.rolling(window=3).mean()

# output
                   A         B         C         D
2000-01-01 -1.527308  0.468773 -0.810878 -1.154924
2000-01-02 -0.860748 -0.426511  1.646501 -0.136477
2000-01-03  0.634766 -0.893297 -0.278013  0.332552
2000-01-04  1.420817  1.290515 -0.332443 -0.671766
2000-01-05 -0.337540  0.982137 -0.537922 -0.174218
2000-01-06 -0.553567  0.326873 -0.428166  0.413263
2000-01-07  1.417336 -2.069682  1.409965 -0.204691
2000-01-08 -0.280715 -1.224854 -0.781816 -1.101787
2000-01-09  0.508010  0.832045 -0.365776 -0.096992
2000-01-10 -0.824893  2.308766  0.260663 -1.174649
                   A         B         C         D
2000-01-01       NaN       NaN       NaN       NaN
2000-01-02       NaN       NaN       NaN       NaN
2000-01-03 -0.584430 -0.283678  0.185870 -0.319616
2000-01-04  0.398278 -0.009765  0.345348 -0.158564
2000-01-05  0.572681  0.459785 -0.382793 -0.171144
2000-01-06  0.176570  0.866508 -0.432844 -0.144240
2000-01-07  0.175410 -0.253557  0.147959  0.011452
2000-01-08  0.194351 -0.989221  0.066661 -0.297738
2000-01-09  0.548210 -0.820830  0.087458 -0.467823
2000-01-10 -0.199199  0.638652 -0.295643 -0.791143
```

<b>Expanding</b>

```
df.expanding(min_periods=3).mean()
```

### Aggregation functions

Aggregate functions will apply any window operations to it 

```
df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print (df)
r = df.rolling(window=3,min_periods=1)
print (r.aggregate(np.sum))
```