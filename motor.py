import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()


    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        if self.jointName == "Torso_FrontLeg":
            self.frequency *= .5
        self.offset = c.phaseOffset
        self.motorValues = c.amplitude * np.sin(self.frequency * np.linspace(0, 2*np.pi, c.num_steps) + self.offset)
    

    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],
            maxForce=50
        )
    
    def Save_Values(self):
        np.save(f"data/{self.jointName}MotorValues.npy", self.motorValues)