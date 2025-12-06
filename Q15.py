import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

wn = 2.0
zeta = 0.2

def deriv(y, t):
    theta, omega = y
    dtheta = omega
    domega = -2*zeta*wn*omega - (wn**2)*theta
    return [dtheta, domega]

tspan = np.linspace(0,20,1000)
y0 = [1.0, 0.0]
sol = odeint(deriv, y0, tspan)

theta = sol[:,0]
plt.plot(tspan, theta)
plt.show()
