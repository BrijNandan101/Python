#step-1 creating sample data frame
import pandas as pd

data = {
    "Name":['Brij','Shree','Aman','Anurag']
    ,"Age":[25,23,24,22],
    "Salary":[50000,45000,30000,30000]
    ,"Performance Score":[90,80,70,85]
    ,"Department":["HR","IT","HR","IT"]
}

df=pd.DataFrame(data)
print(df)
print(df.describe(),sep="    \t")
print(df.describe(include="all"),sep="   \t")