import numpy as np
#assuming two numpy arrays arr1 and arr2
# arr1=np.array([[1,2],[3,4]])
# arr2=np.array([[1,2],[3,4]])
arr1=np.random.randint(0,10,10)
print("Array1:")
print(arr1)
arr2=np.random.randint(0,10,10)
print("Array2:")
print(arr2)
print("Gonna test the equality now :")
is_equal=np.allclose(arr1,arr2)
print(is_equal)