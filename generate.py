#Start
import pyrosim.pyrosim as pyrosim
import random


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

def Generate_Body(): 

    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name='Torso', pos=[1.5,0,1.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [1,0,1])
    pyrosim.Send_Cube(name='Backleg', pos=[-.5,0,-0.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [2, 0, 1])
    pyrosim.Send_Cube(name='Frontleg', pos=[0.5,0,-0.5] , size=[1,1,1])

    pyrosim.End()



def Generate_Brain(): 

    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")


    for neurons in range(3):
        for motors in range(3, 5):
            pyrosim.Send_Synapse( sourceNeuronName = neurons , targetNeuronName = motors , weight = (random.random()*2-1) )

    pyrosim.End()



Generate_Body()
Generate_Brain()


