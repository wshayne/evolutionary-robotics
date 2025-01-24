import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[-3,3,.5], size=[1,1,1])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Link_0", pos=[0, 0, 0.5], size=[1, 1, 1])
    pyrosim.Send_Cube(name="Link_1", pos=[0,0,.5], size=[1,1,1])
    pyrosim.Send_Joint(name="Link_0_Link_1", parent="Link_0", child="Link_1", type="revolute", position=[0, 0, 1.0])
    pyrosim.Send_Joint(name="Link_1_Link_2", parent="Link_1", child="Link_2", type="revolute", position=[0,0,1])
    pyrosim.Send_Cube(name="Link_2", pos=[0,0,.5], size=[1,1,1])
    pyrosim.Send_Joint(name="Link_2_Link_3", parent="Link_2", child="Link_3", type="revolute", position=[0,.5,.5])
    pyrosim.Send_Cube(name="Link_3", pos=[0,.5,0], size=[1,1,1])
    pyrosim.Send_Joint(name="Link_3_Link_4", parent="Link_3", child="Link_4", type="revolute", position=[0,1,0])
    pyrosim.Send_Cube(name="Link_4", pos=[0,.5,0], size=[1,1,1])
    pyrosim.Send_Joint(name="Link_4_Link_5", parent="Link_4", child="Link_5", type="revolute", position=[0,.5,-.5])
    pyrosim.Send_Cube(name="Link_5", pos=[0,0,-.5], size=[1,1,1])
    pyrosim.Send_Joint(name="Link_5_Link_6", parent="Link_5", child="Link_6", type="revolute", position=[0,0,-1])
    pyrosim.Send_Cube(name="Link_6", pos=[0,0,-.5], size=[1,1,1])
    pyrosim.End()

if __name__ == "__main__":
    Create_World()
    Create_Robot()