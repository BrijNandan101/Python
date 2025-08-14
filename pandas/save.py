import pandas as pd

# making data set using dictionary
data = {
    "Name":['Ram', 'shyam', 'ghanshyam'],
    "Age":['10','20','30'],
    "City":['Nagpur','Allahabad','Delhi']
}

#defining data frame
df = pd.DataFrame(data)

#displaying data frame
print(df)

#saving data frame
df.to_csv("output.csv")