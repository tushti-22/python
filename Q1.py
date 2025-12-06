import numpy as np
import scipy.stats as stats

arr = np.random.randn(1000)
print(arr)
mean = np.mean(arr)
median = np.median(arr)
variance = np.var(arr)

print(f"Mean: {mean}, Median: {median}, Variance: {variance}")
