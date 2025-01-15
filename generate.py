import pyrosim.pyrosim as pyrosim

(length, width, height) = (1, 1, 1)
(x, y, z) = (0, 0, .5)

pyrosim.Start_SDF("boxes.sdf")
for a in range(5):
    for b in range(5):
        for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x+a,y+b,z+i], size=[length*.9**i,width*.9**i,height*.9**i])
pyrosim.End()