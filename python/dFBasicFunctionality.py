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
