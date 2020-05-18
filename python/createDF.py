import pandas as pd


# Creating Empty Dataframe
print(" \nCreating Empty Dataframe")
df = pd.DataFrame()
print (df)

# Creating a dataframe from list

print("\nCreating a dataframe from list")
data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data)
print (df)

# Creating a dataframe from 2d list
print("\nCreating a dataframe from 2d list")
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print (df)

# Creating a dataframe and changing the datatype
print("\nCreating a dataframe and changing the datatype")
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print (df)

# Create a DataFrame from Dict of ndarrays / Lists
print("\n Create a DataFrame from Dict of ndarrays / Lists")
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print (df)

# Create a DataFrame from List of Dicts
print("\n Create a DataFrame from list of dicts")
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print (df)

