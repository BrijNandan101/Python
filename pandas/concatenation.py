"""
vertically(row-wise)
horizintally(column-wise)

pd.concate([df1,df2],axis=0, ignore_index=True)



"""

import pandas as pd

#region 1

df_region1=pd.DataFrame({
    "Customer_id":[1,2,3,4,5],
    "Region":["North","South","East","West","North"]
})
df_region2 = pd.DataFrame({
    "Customer_id":[6,7,8,9,10],
    "Name":['Brij','Nishant','Saurabh','Saurabh','Nishant']
})

#concatenate vertically
df_region3=pd.concat([df_region1,df_region2],axis=0, ignore_index=True)
print(df_region3)

#concatenate horizonatally
df_region4=pd.concat([df_region1,df_region2],axis=1, ignore_index=True)
print(df_region4)