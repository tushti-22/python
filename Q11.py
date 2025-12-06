import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, interpolate

years = np.array([2000,2005,2010,2015,2020])
pop = np.array([50,55,70,80,90])

r, _ = stats.pearsonr(years, pop)
print("Pearson r:", r)

f = interpolate.interp1d(years, pop, kind='linear')
xnew = np.arange(2000,2021)
ynew = f(xnew)

plt.plot(years, pop, 'o')
plt.plot(xnew, ynew, '-')
plt.show()
