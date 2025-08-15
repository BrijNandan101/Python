import pandas as pd

#customer dataframe
df_customers=pd.DataFrame({
    "Customer_Id":[101,102,103,104],
    "Name":['Brij','Aprajita','Anurag','Aman']
})
df_orders=pd.DataFrame({
    "Customer_Id":[101,102,105,106],
    "Order_Amount":[300,850,120,250]
})

#merging
merged=pd.merge(df_customers,df_orders, on="Customer_Id", how="inner")
print(merged)
merged=pd.merge(df_customers,df_orders, on="Customer_Id", how="outer")
print(merged)
merged=pd.merge(df_customers,df_orders, on="Customer_Id", how="right")
print(merged)
merged=pd.merge(df_customers,df_orders, on="Customer_Id", how="left")
print(merged)
merged=pd.merge(df_customers,df_orders, how="cross")
print(merged)