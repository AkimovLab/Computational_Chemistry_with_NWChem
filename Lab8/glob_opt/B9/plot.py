import numpy as np
import matplotlib.pyplot as plt

sp = np.loadtxt("b9.10.emotion")

fig = plt.figure(num=1)
plt.plot(sp[:, 0], sp[:, 1], color="blue", label="Total energy")
plt.plot(sp[:, 0], sp[:, 2], color="black", label="Potential energy")
plt.xlabel("Time, a.u.")
plt.ylabel("Energy, a.u.")
plt.legend()
plt.savefig("progress-e.png")


fig = plt.figure(num=2)
plt.plot(sp[:, 0], sp[:, 18], color="blue", label="Temperature")
plt.xlabel("Time, a.u.")
plt.ylabel("Temperature, K")
plt.legend()
plt.savefig("progress-t.png")
