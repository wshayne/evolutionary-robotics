import numpy as np
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from simulate import simulate
import os
import time
import constants as c
import random

class SOLUTION:
    def __init__(self):
        self.weights = np.random.random((c.numSensorNeurons, c.numMotorNeurons))
        self.weights = self.weights * 2 - 1
        self.myID = np.random.randint(100000)
        self.Create_Brain()
        self.brain = NEURAL_NETWORK(f"brain{self.myID}.nndf")
        os.remove(f"brain{self.myID}.nndf")
    
    def Evaluate(self, directOrGUI, target):
        self.fitness = simulate(self.brain, directOrGUI, target)
        return self.fitness

    def Mutate(self):
        synapse = random.choice(list(self.brain.synapses.keys()))
        new_val = np.random.uniform() * 2 - 1
        self.brain.synapses[synapse].weight = new_val
        self.weights[int(synapse[0]), int(synapse[1]) - c.numSensorNeurons] = new_val
    
    def Set_ID(self, ID):
        self.myID = ID
    
    @staticmethod
    def Create_World():
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-3,3,.5], size=[1,1,1])
        pyrosim.End()

    @staticmethod
    def Create_Body():
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1,1,1])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2,1,0.2])
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2,1,0.2])
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position=[-0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg",pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg",pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute", position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg",pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute", position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg",pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        links = ["Torso", "BackLeg", "FrontLeg", "LeftLeg", "RightLeg", "FrontLowerLeg", "BackLowerLeg", "LeftLowerLeg", "RightLowerLeg", "targetX", "targetY"]
        for i in range(len(links)):
            pyrosim.Send_Sensor_Neuron(name=i, linkName=links[i])
        joints = ["Torso_BackLeg", "Torso_FrontLeg", "Torso_LeftLeg", "Torso_RightLeg", "FrontLeg_FrontLowerLeg", "BackLeg_BackLowerLeg", "LeftLeg_LeftLowerLeg", "RightLeg_RightLowerLeg"]
        for i in range(len(joints)):
            pyrosim.Send_Motor_Neuron(name=i+len(links), jointName=joints[i])
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()