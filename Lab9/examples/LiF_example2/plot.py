import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(num=1)
sp = np.loadtxt("LiF_IR.dat", skiprows=1)
plt.plot(sp[:, 0], sp[:, 1], color="blue", label="IR spectrum")
plt.xlabel("Wavenumber, $cm^{-1}$")
plt.ylabel("Intensity, arb. units")
plt.legend()
plt.savefig("LiF_IR.png")


fig = plt.figure(num=2)
sp = np.loadtxt("LiF_VDOS.dat", skiprows=1)
plt.plot(sp[:, 0], sp[:, 1], color="blue", label="Li vDOS")
plt.plot(sp[:, 0], sp[:, 2], color="purple", label="F vDOS")
plt.plot(sp[:, 0], sp[:, 3], color="black", label="Total vDOS")
plt.xlabel("Wavenumber, $cm^{-1}$")
plt.ylabel("VDOS, 1/$cm^{-1}$")
plt.legend()
plt.savefig("LiF_VDOS.png")
