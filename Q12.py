import numpy as np
import matplotlib.pyplot as plt

coeffs = [3, -5, 2, -8]
roots = np.roots(coeffs)
print("Roots:", roots)

x = np.linspace(-3,3,400)
pvals = np.polyval(coeffs, x)

plt.plot(x, pvals)
plt.axhline(0, color='k')
plt.show()
