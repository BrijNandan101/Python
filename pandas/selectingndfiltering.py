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

print("Names(Single column return series)")
print(df["Name"])

print("Names and Salary")
print(df[["Name","Salary"]],sep="\n")

#or

subset=df[["Name","Salary"]]
print(subset)

#fitering using single condition
high_salary=df[df["Salary"]>30000]
print(high_salary)

#filtering using multiple condition
high_salary=df[(df["Salary"]>30000) & (df["Age"]>22)]
print(high_salary)

#if we want only one condition to be true out of two we use or in place of and
high_salary=df[(df["Salary"]>30000) | (df["Age"]>22)]
print(high_salary)