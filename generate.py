import pyrosim.pyrosim as pyrosim

(length, width, height) = (1, 2, 3)
(x, y, z) = (0, 0, 1.5)

pyrosim.Start_SDF("box.sdf")
pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])
pyrosim.End()