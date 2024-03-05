# Dictonary:

import pandas as pd

Dict = pd.DataFrame({"Ansh":[78,65,80],"Nitish":[55,69,94],"Yug":[100,85,42]}, 
                    index=["Maths", "Physics", "Computer"])

print(Dict)                 #Creating DataFrame

# print(Dict.index)           Finding indexs of Dictonaries
# print(Dict.values)          Finding values of Dictonaries
# print(Dict.size)            Finding size of Dictonaries
# print(Dict.shape)           Finding shape means (rows,columns) of Dictonaries

# print(Dict.Ansh["Maths"]) --Finding individual Value

"""
Dict.Ansh["Maths"] = 98      --changing value of individual
print(Dict)
"""




