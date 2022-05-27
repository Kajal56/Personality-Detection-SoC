import numpy as np
arr1=np.random.randint(0,10,(3,3))
print("array 1 is :")
print(arr1)
arr2=np.random.randint(0,10,(3,3))
print("array 2 is :")
print(arr2)
print("----------below is the required array (ie. (A+B)*(-A/2))--------------")

print((arr1+arr2)*(arr1/(-2)))