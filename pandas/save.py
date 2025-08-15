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

#saving data frame in CSV file
df.to_csv("output.csv") #if we dont want the indexing we d0 df.to_csv("filename.filetype", indexing=False)

#saving dataframe in Excel file
df.to_excel("filename.filetype", index=True or False)

#saving dataframe in JSON file
df.to_json("filename.filetype", index=True or False)