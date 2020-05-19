import pandas as pd

print("Make an existing column dtype='categorical'")
s = pd.Series(["a", "b", "c", "a"], dtype="category")
print(s)

cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
print(cat)

print('Create a new Ordered Categorical series')
dog =pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'],ordered=True)
print (dog)

# Get Categories
print(dog.categories)

# rename Categories
s.cat.categories = ['Group 1','Group 2', 'Group 3']

# Add Categories
s = s.cat.add_categories([4])

# Delete Categories
s.cat.remove_categories("a")
