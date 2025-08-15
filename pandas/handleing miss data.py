"""
drop()  method

df.dropna(axis=0, inplace=True)  #for rows axis => 0

df.dropna(axis=1, inplace=True)    #for cols axis => 1
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

df.dropna(inplace=True)
print(df)