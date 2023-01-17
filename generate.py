#Start
import pyrosim.pyrosim as pyrosim


def Create_Robot(): 

    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name='Torso', pos=[1.5,0,1.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [1,0,1])
    pyrosim.Send_Cube(name='Backleg', pos=[-.5,0,-0.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [2, 0, 1])
    pyrosim.Send_Cube(name='Frontleg', pos=[0.5,0,-0.5] , size=[1,1,1])

    pyrosim.End()



def Create_World():
    pyrosim.Start_SDF("world.sdf")



    pyrosim.Send_Cube(name="box", pos=[0,5,0] , size=[1,1,1])

    pyrosim.End()

Create_World()
Create_Robot()