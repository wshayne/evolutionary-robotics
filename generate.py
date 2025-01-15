import pyrosim.pyrosim as pyrosim

(length, width, height) = (1, 1, 1)
(x, y, z) = (0, 0, .5)

pyrosim.Start_SDF("boxes.sdf")
pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])
pyrosim.Send_Cube(name="Box2", pos=[x+1,y,z+1], size=[length,width,height])
pyrosim.End()