from numpy import *
arr1 = array([1,2,4,5])
arr2 = arr1.view()
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))