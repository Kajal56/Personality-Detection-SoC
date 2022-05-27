import numpy as np
from math import sqrt
arr=np.random.randint(0,50,(10,2))
print(arr)
arr_polar=np.ones((10,2))
# print(arr_polar)
arr_polar[:,0]=np.sqrt(arr[:,0]*arr[:,0]+arr[:,1]*arr[:,1])
arr_polar[:,1]=np.arctan(arr[:,1]/arr[:,0])
print("-------------below is the array containing polar co-ordinates---------------")
print(arr_polar)