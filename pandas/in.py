import pandas as pd

df = pd.read_csv(r"D:\Python\pandas\Netflix Dataset.csv", encoding="utf-8")

print("displaying the info of the dataset")

print(df.info())

data = {
    "Name":['Ram', 'shyam', 'ghanshyam'],
    "Age":['10','20','30'],
    "City":['Nagpur','Allahabad','Delhi']
}

#defining data frame
df = pd.DataFrame(data)

print(df.info())