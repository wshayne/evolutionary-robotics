import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR
import os
import constants as c

class ROBOT:

    def __init__(self, nn):
        self.robot = p.loadURDF("body.urdf")
        self.nn = nn
        pyrosim.Prepare_To_Simulate(self.robot)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        for name, neuron in self.nn.neurons.items():
            if neuron.Is_Sensor_Neuron():
                if neuron.Get_Link_Name() == "posX":
                    self.xNeuron = name
                if neuron.Get_Link_Name() == "posY":
                    self.yNeuron = name


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
        pos = self.Get_Position()
        self.nn.neurons[self.xNeuron].Set_Value(pos[0])
        self.nn.neurons[self.yNeuron].Set_Value(pos[1])
        # self.nn.Print()
    

    def Get_Position(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        basePosition = basePositionAndOrientation[0]
        return basePosition[:2]