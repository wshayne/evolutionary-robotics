import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

amplitude_FrontLeg = np.pi/6
frequency_FrontLeg = 12
phaseOffset_FrontLeg = 0
amplitude_BackLeg = np.pi/6
frequency_BackLeg = 12
phaseOffset_BackLeg = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

num_steps = 1000

backLegSensorValues = np.zeros(num_steps)
frontLegSensorValues = np.zeros(num_steps)

targetAngles = np.linspace(0, 2*np.pi, num_steps)
targetAngles_FrontLeg = amplitude_FrontLeg * np.sin(frequency_FrontLeg*targetAngles + phaseOffset_FrontLeg)
targetAngles_BackLeg = amplitude_BackLeg * np.sin(frequency_BackLeg*targetAngles + phaseOffset_BackLeg)
# np.save("data/targetAngles_FrontLeg.npy", targetAngles_FrontLeg)
# np.save("data/targetAngles_BackLeg.npy", targetAngles_BackLeg)

for i in range(num_steps):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = 'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles_BackLeg[i],
        maxForce = 50
    )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = 'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles_FrontLeg[i],
        maxForce = 50
    )
    time.sleep(1/60)

p.disconnect()

np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)