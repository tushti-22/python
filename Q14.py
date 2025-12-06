import numpy as np
import matplotlib.pyplot as plt

def f(x): return x**4 - 3*x**3 + 2
def df(x): return 4*x**3 - 9*x**2

crit = np.roots([4, -9, 0, 0])
crit_real = [r.real for r in crit if abs(r.imag) < 1e-8]
print("Critical points:", crit_real)

x = np.linspace(-2,3,400)
y = f(x)

plt.plot(x, y)
plt.show()
