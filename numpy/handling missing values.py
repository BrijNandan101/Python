#np.isnana(array)
import numpy as np

arr=np.array([1,2,np.nan,4,5])
print(arr)
print(np.isnan(arr))
print(np.isfinite(arr))
print(np.isinf(arr))
# print(np.nan==np.nan) it cant be done because it is not a number

#nan to num
print(np.nan_to_num(arr))
# print(np.nan_to_num(100)) it cant be done because it is not a number  
print(np.nan_to_num(arr,100.0))

#isinfinite
arr=np.array([1,2,np.inf,4,5, -np.inf])
print(arr)
print(np.isfinite(arr))
print(np.isinf(arr))
print(np.isfinite(arr))
print(np.isinf(arr))

cleaned_arr=np.nan_to_num(arr,posinf=100,neginf=-100)
print(cleaned_arr)