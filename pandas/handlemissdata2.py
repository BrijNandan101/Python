"""
when we want to fill data in place of none of NaN data

we use fill()  Method
fillna(value, inplace=True)
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

# df.fillna(0, inplace=True)
# print(df)

#if we want to pass some calculated value
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print(df)