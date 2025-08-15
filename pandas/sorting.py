#sorting data

#sorting data in one column
#df.sort_values(by="Column_Name", True(Ascending)/False(Descending), inplace=True/False)

import pandas as pd

data={
    "Name":['Arun','Varun','Karun']
    ,"Age":[28,34,22],
    "Salary":[20000, 15000,25000]
}

df=pd.DataFrame(data)
print(df)

df.sort_values(by="Age", ascending=True, inplace=True)
print("sort age by ascending")
print(df)