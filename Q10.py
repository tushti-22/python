import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

tdata = np.array([0,1,2,3,4,5], dtype=float)
vdata = np.array([2,3.1,7.9,18.2,34.3,56.2], dtype=float)

def quad(t,a,b,c):
    return a*t**2 + b*t + c

popt, _ = optimize.curve_fit(quad, tdata, vdata)
tfine = np.linspace(tdata.min(), tdata.max(), 200)
plt.scatter(tdata, vdata, label='data')
plt.plot(tfine, quad(tfine, *popt), label='fit')
plt.legend(); plt.show()
