import numpy as np
arr=np.random.randint(10,60,15)
print(arr)
mean = np.mean(arr)
median = np.median(arr) 
print("Mean:", mean)
print("Median:", median)
std_dev = np.std(arr)
print("Standard Deviation:", std_dev)