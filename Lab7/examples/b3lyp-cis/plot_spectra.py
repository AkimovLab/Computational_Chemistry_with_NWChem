import numpy as np
import matplotlib.pyplot as plt

#%matplotlib inline

sp = np.loadtxt("spectrum.dat")
sp2 = np.loadtxt("spectrum2.dat")

plt.plot(sp[:, 0], sp[:, 1]*10, color="blue")
plt.plot(sp2[:, 0], sp2[:, 1], color = "black")

plt.savefig("spectra.png")
