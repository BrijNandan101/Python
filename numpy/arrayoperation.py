import numpy as np

#give shape of array
arr_2d=np.array([[1,2],
         [3,4]])
print(arr_2d.shape)

#give size of array like how many elements an array conatains
arr=np.array([[10,20,30],
              [40,50,60]])
print(arr.size)

#to check number of dimensions like 1d , 2d or 3d
arr1=np.array([1,2,3,4])
arr2=np.array([[2,3,4],[5,6,7]])
arr3=np.array([[[1,2],[3,4],[5,6],[7,8]]])

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

#to check datatype
print(arr.dtype)

#to change datatype
arr5=np.array([1.2,3.5,4.0,5.3])
print(arr5.dtype)
change=arr5.astype(int)

print(change)
print(change.dtype)


#operators
print(change+5)
print(change[3]+5)

#boolean masking
arr0=np.array([10,20,30,40,50])
print(arr[arr>20])

#insertion of element in array in numpy
"""
np.insert(array,index,value,axis=None)
array - original array
index -
value -
axis -
axis - 0, row-wise
1, column-wise
"""
new=np.insert(arr0,3,44,0)  #in 1d array
print(new)

arr01=np.array([[1,2],[3,4]])
new2=np.insert(arr01,1,[5,7],axis=0)    #2d
print(new2)