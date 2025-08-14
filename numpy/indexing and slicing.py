import numpy as np

#numpy follows 0 absed indexing also -ve index
"""
array[index] #1D array
array[row, column] #2D array
"""

#indexing
arr=np.array([10,20,30,40,50])
print(arr[0]) #first element
print(arr[2]) #third element
print(arr[-1]) #last element

#slicing
"""
array[start: stop: step]

arr[start:end], start to end -1

negative step -1 reverse
"""
arr1=np.array([10,20,30,40,50])
print(arr1[1:5])  #from index 1 to 5
print(arr1[:4])   #from index 0 to 3 total 4
print(arr1[::2])    #interval of 2
print(arr1[::-1])   #reverse order


#fancy indexing
arr2=np.array([10,20,30,40,50])
print(arr2[[0,2,4]])    #multiple index at same time