#head(n) method, tail(n) method
#head() 5
#tail(n)    5

import pandas as pd

df = pd.read_csv(r"D:\Python\pandas\Netflix Dataset.csv", encoding="utf-8")

print("display 10 rows from top")
print(df.head(10))    #by default it will display 5 rows    #pass int values

print("display 10 rows from bottom")
print(df.tail(10))  #by default it will display 5 rows #pass int values