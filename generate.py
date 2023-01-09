#Start
import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")



for j in range(5):
    for k in range(5):
        size = 1 
        for i in range(10):

            
            size = 0.90**i
            pyrosim.Send_Cube(name="boxes.sdf", pos=[k,j,i] , size=[size,size,size])

pyrosim.End()