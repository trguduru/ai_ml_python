import pandas as pd
s = pd.Series([1,2,3,4,4,5,5,6,6,3,2,1])
print(s)
print(type(s))

# retrieve
print(s[0])  # index based get

# contains
print(1 in s)  # checks whether the index/key is available or not

# arithmetic operations
#print( s * 2)  # multiplies the series values by 2

# print(s **2)  # square

print(s.mean())
print(s.median())
print(s.nunique())
print(s.unique())
