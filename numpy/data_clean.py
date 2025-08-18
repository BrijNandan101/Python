#importing necessary libraries
import pandas as pd
import numpy as np

#loading the dataset
df=pd.read_csv(r'D:\Python\pandas\Netflix Dataset.csv',encoding="utf-8")
print(df.head())

#checking missing values
print('missing values in each coliumn')
print(df.isnull().sum())

df['Release_Date'].fillna(df['Release_Date'],inplace=True)

print(df.isnull().sum())