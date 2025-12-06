import numpy as np
arr4 = np.arange(10,26).reshape(4,4)
print("Original Array\n" , arr4)
print(arr4[1])
print(arr4[:,-1])
arr4[0] = 0
print(arr4)
