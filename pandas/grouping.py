import pandas as pd

data={
    "Name":['Arun','Varun','Karun','Tarun','Marun']
    ,"Age":[28,34,22,32,28],
    "Salary":[20000, 15000,25000,35000,80000]
}

df=pd.DataFrame(data)
print(df)

grouped=df.groupby("Age")["Salary"].sum()
print(grouped)