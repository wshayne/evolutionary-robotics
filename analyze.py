import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")

plt.plot(backLegSensorValues, label="Back Leg", lw=2)
plt.plot(frontLegSensorValues, label="Front Leg")
plt.legend()
plt.show()

targetAngles_FrontLeg = np.load("data/targetAngles_FrontLeg.npy")
targetAngles_BackLeg = np.load("data/targetAngles_BackLeg.npy")
plt.plot(targetAngles_FrontLeg, label="targetAngles_FrontLeg")
plt.plot(targetAngles_BackLeg, label="targetAngles_BackLeg")
plt.title("Motor Commands")
plt.legend()
plt.show()