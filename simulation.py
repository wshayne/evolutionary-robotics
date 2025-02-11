from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import time

class SIMULATION:

    def __init__(self, directOrGUI):
        self.directOrGUI = directOrGUI
        if self.directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        elif self.directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI)
        else:
            raise(Exception("No DIRECT/GUI argumeng supplied"))
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.world = WORLD()
        self.robot = ROBOT()
        p.setGravity(0,0,-9.8)


    def Run(self):
        for i in range(c.num_steps):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            if self.directOrGUI == "GUI":
                time.sleep(1/120)
    

    def Get_Fitness(self):
        self.robot.Get_Fitness()
    

    def __del__(self):
        p.disconnect()