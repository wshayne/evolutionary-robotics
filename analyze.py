import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load("data/BackLegSensorValues.npy")

plt.plot(backLegSensorValues)
plt.show()