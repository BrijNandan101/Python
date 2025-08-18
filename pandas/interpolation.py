"""
it is a method through which in place of missing values we can put estimated values.
based on mathematical operations

why use it?
1- preerve data integrity
2- smooth trends
3- avoid data loss
"""
import pandas as pd

data = {
    "Name":['Brij','Shree','Aman','Anurag']
    ,"Age":[25,23,24,None],
    "Salary":[50000,45000,30000,None]
    ,"Performance Score":[90,80,70,None]
    ,"Department":["HR","IT","HR",None]
}

df=pd.DataFrame(data)
print(df)

df.interpolate(method='linear', axis=0, inplace=True)     #linerar , polunomial, line
