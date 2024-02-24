#List:

# List
import pandas as pd

# lst = pd.Series([0,1,2,3,4,5]) --Creating list

lst = pd.Series([0,1,2,3,4,5], index = ["a", "b", "c", "d", "e", "f"]) #Changing index values
print(lst)

# print(lst[4]) --return value

# print(lst.values) --return values
# print(lst.index) --return indexs
# print(lst.shape) --return shape
# print(lst.size) --return size

# print(lst.dtype) --return datatype

"""
lst[0] = 7
print(lst)  --modify list
"""

# print(lst.sort_values(ascending=False)) --sorting the values of list



