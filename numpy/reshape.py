"""
reshape[rows, cols ] specify new shape
if dimensions match
"""
import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
reshaped_arr=arr.reshape(3,3)
print(reshaped_arr)