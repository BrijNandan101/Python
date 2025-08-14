#head(n) method, tail(n) method
#head() 5
#tail(n)    5

import pandas as pd

df = pd.read_csv(r"D:\Python\pandas\Netflix Dataset.csv", encoding="utf-8")

print("display 10 rows from top")
print(df.head(10))

print("display 10 rows from bottom")
print(df.tail(10))