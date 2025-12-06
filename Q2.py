import numpy as np
from scipy import fftpack

a2 = np.random.rand(8,8)
dft2 = fftpack.fft2(a2)
print("DFT of 2D array:\n", dft2)
