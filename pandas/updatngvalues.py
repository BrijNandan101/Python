import pandas as pd

#method 1 of updating values

data = {
    "Name":['Brij','Shree','Aman','Anurag']
    ,"Age":[25,23,24,22],
    "Salary":[50000,45000,30000,30000]
    ,"Performance Score":[90,80,70,85]
    ,"Department":["HR","IT","HR","IT"]
}

df=pd.DataFrame(data)
print(df)

#if we want to update value of a certain index
#we use  .loc[]
#df.loc[row_index,"column_name"]=new_value

df.loc[0,"Salary"]=60000
print(df)

#method 2  =>if we want to update multiple values of a column
#df['Column_name']=df['Column_name']*value
df['Salary']=df["Salary"]*1.5
print(df)