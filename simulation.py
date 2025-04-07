from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import time
import numpy as np

class SIMULATION:

    def __init__(self, directOrGUI, brain, target):
        self.target = target
        self.directOrGUI = directOrGUI
        if self.directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        elif self.directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI)
        else:
            raise(Exception("No DIRECT/GUI argument supplied"))
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        time.sleep(0.01)
        self.world = WORLD()
        self.positions = []
        for neuron in brain.neurons.values():
            if neuron.Is_Sensor_Neuron():
                if neuron.linkName == 'targetX':
                    neuron.Set_Value(target[0])
                elif neuron.linkName == 'targetY':
                    neuron.Set_Value(target[1])
        self.robot = ROBOT(brain)
        p.setGravity(0,0,-9.8)


    def Run(self):
        for i in range(c.num_steps):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            self.positions.append(self.robot.Get_Position())
            if self.directOrGUI == "GUI":
                time.sleep(1/120)
    

    def Get_Fitness(self):
        fitness = 0
        for pos in self.positions:
            fitness += np.linalg.norm(np.array(pos) - np.array(self.target))
        return fitness
    

    def __del__(self):
        p.disconnect()