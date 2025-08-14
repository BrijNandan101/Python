import pandas as pd

# 1. Create a DataFrame
# df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# print(df)

# 2. read data from CSV file into the dataframe
df = pd.read_csv(r"D:\Python\pandas\Netflix Dataset.csv", encoding="utf-8")
print(df)