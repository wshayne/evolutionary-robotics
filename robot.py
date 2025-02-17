import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR
import os
import constants as c

class ROBOT:

    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.robot = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")
        os.remove(f"brain{solutionID}.nndf")
        pyrosim.Prepare_To_Simulate(self.robot)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()


    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)


    def Sense(self, t):
        for sensor in self.sensors.values():
            sensor.Get_Value(t)
    

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(self.robot, desiredAngle)
    

    def Save_Values(self):
        for sensor in self.sensors.values():
            sensor.Save_Values()
    
    def Think(self):
        self.nn.Update()
        # self.nn.Print()
    

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robot, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        with open(f"tmp{self.solutionID}.txt", "w") as f:
            f.write(str(xCoordinateOfLinkZero))
        os.rename(f"tmp{self.solutionID}.txt", f"fitness{self.solutionID}.txt")