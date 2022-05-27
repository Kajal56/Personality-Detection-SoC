import numpy as np
#assuming two numpy arrays arr1 and arr2
arr1=np.array([[1,2,5],[3,4,6]])
arr2=np.array([[5,2],[3,4]])
print("array 1 is :")
print(arr1)

print("array 2 is :")
print(arr2)
final_array= np.intersect1d (arr1,arr2)
print("Final array containing common elements is :")
print(final_array)