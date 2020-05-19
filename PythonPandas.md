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


