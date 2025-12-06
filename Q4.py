import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x = np.linspace(0,10,11)
y = np.sin(x)
f_cubic = interpolate.interp1d(x,y,kind='cubic')

xnew = np.linspace(0,10,201)
y_cub = f_cubic(xnew)

plt.plot(x, y, 'o', label='data')
plt.plot(xnew, y_cub, '-', label='cubic interp')
plt.legend(); plt.show()
