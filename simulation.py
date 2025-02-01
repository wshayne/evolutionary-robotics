from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import time

class SIMULATION:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.world = WORLD()
        self.robot = ROBOT()
        p.setGravity(0,0,-9.8)


    def Run(self):
        for i in range(c.num_steps):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)
        #     pyrosim.Set_Motor_For_Joint(
        #         bodyIndex = robotId,
        #         jointName = 'Torso_BackLeg',
        #         controlMode = p.POSITION_CONTROL,
        #         targetPosition = targetAngles_BackLeg[i],
        #         maxForce = 50
        #     )
        #     pyrosim.Set_Motor_For_Joint(
        #         bodyIndex = robotId,
        #         jointName = 'Torso_FrontLeg',
        #         controlMode = p.POSITION_CONTROL,
        #         targetPosition = targetAngles_FrontLeg[i],
        #         maxForce = 50
        #     )
            time.sleep(1/60)
    

    def __del__(self):
        p.disconnect()