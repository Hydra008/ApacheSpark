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

<b>Creating a dataframe from 2D list
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