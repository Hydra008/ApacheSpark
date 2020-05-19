import pandas as pd
left = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
   {'id':[1,2,3,4,5],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print (left)
print (right)

# Simple Join on just ID
print(pd.merge(left, right, on='subject_id'))

# Simple join on multiple common columns
print(pd.merge(left, right, on=['subject_id', 'id']))

# left join - all keys from left column
print(pd.merge(left, right, on=['subject_id'], how='left'))
# right join - all keys from right column
print(pd.merge(left, right, on=['subject_id'], how='right'))
# outer join - union of keys
print(pd.merge(left, right, on=['subject_id'], how='outer'))
# inner join - intersection of keys
print(pd.merge(left, right, on=['subject_id'], how='inner'))