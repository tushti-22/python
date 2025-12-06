import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter

fs = 500
t = np.linspace(0,1,fs,endpoint=False)
sig = np.sin(2*np.pi*5*t) + 0.5*np.sin(2*np.pi*80*t)

numtaps = 101
cutoff = 20
fir = firwin(numtaps, cutoff/(fs/2))
filtered = lfilter(fir, 1.0, sig)

plt.plot(t, sig, label='noisy')
plt.plot(t, filtered, label='filtered')
plt.legend(); plt.show()
