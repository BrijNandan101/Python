#adding new columns in pandas
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

#using assingment
#square brackets df["columnn_Name"]=some data
df["Bonus"]=df['Salary']*0.1
print(df)

#using insert method used in comapnies
#df.insert(location, "col_name", somedata)
df.insert(0,"Employee ID",[101,102,103,104])
print(df)