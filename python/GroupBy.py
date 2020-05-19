import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
print(df)

# Group by teams & Year
df.groupby(['Team', 'Year'])
# Group by year
groupedByYear = df.groupby('Year')

for name,group in groupedByYear:
   print (name)
   print (group)

# Selecting a group
year2014 = groupedByYear.get_group(2014)
print(year2014)
print(year2014['Points'].sum())

# Transformations on grouped data

# Aggregation
print(groupedByYear.agg(np.mean))
print(groupedByYear.agg([np.sum, np.mean]))
print(groupedByYear.apply(np.mean))

# Transformation
print(groupedByYear.transform(lambda x: x/2))

# filter
#print(df.groupby('Year').filter(lambda x: x['Points'].filter() >= 500))