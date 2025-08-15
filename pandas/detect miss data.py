"""
NaN (Not a Number)
None(For Object data Types)
"""
"""
we use isnull() method
if True => NaN is missing
if False => value is present
"""
import pandas as pd

data = {
    "Name":['Brij','Shree','Aman',None]
    ,"Age":[25,23,24,None],
    "Salary":[50000,45000,30000,None]
    ,"Performance Score":[90,80,70,None]
    ,"Department":["HR","IT","HR",None]
}

df=pd.DataFrame(data)
print(df)

print(df.isnull())

print(df.isnull().sum())  #returns the number of missing values