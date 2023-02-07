import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c
class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons)*2-1

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        
        os.system("python3 simulate.py " +directOrGUI +  " " + str(self.myID)  + "2&>1 &")
        fitnessFileName = "fitness" + str(self.myID)+".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)

        file = open(fitnessFileName, "r")
        
        self.fitness = float(file.read())
        file.close()

    def Start_Simulation(self, directOrGUI):
        self.Generate_Body()
        self.Generate_Brain()
        systemCommand = "python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &"
        os.system(systemCommand)
    
    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)

        file = open(fitnessFileName, "r")
        self.fitness = float(file.read())
        file.close()
        #print(self.fitness)
        os.system("rm " + fitnessFileName)
    def Mutate(self):
        row1 = random.randint(0,c.numSensorNeurons-1)
        col1 = random.randint(0,c.numMotorNeurons-1)
        self.weights[row1, col1] = random.random()*2-1
    def Get_Fitness(self):
        return self.fitness  
    def Set_ID(self, newID):
        self.myID = newID
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")



       # pyrosim.Send_Cube(name="box", pos=[0,5,0] , size=[1,1,1])

        pyrosim.End()

    def Generate_Body(self): 
        '''
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name='Torso', pos=[0,0,1] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [0,-0.5,1] , jointAxis = "1 0 0")
        pyrosim.Send_Cube(name='Backleg', pos=[0,-0.5,0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [0, 0.5, 1] , jointAxis = "1 0 0" )
        pyrosim.Send_Cube(name='Frontleg', pos=[0,0.5,0] , size=[0.2,1,0.2])
        pyrosim.End()
        '''
        pyrosim.Start_URDF("body.urdf")
        # dimensions of the box
        length, width, height = 1.5, 2, 1
        pyrosim.Send_Cube(name='Torso', pos=[0,0,1] , size=[length,width,height])

        pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [0,0,1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='Backleg', pos=[0,-1,0] , size=[0.6,0.6,0.6])
        pyrosim.Send_Joint( name = "Backleg_BackLowerleg" , parent= "Backleg" , child = "BackLowerleg" , type = "revolute", position = [0,-0.5,-0.5], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='BackLowerleg', pos=[0,0,0] , size=[0.2,0.2,1])
     
        pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='Frontleg', pos=[0,0.5,0] , size=[0.2,0.2,0.2])
        pyrosim.Send_Joint( name = "Frontleg_FrontLowerleg" , parent= "Frontleg" , child = "FrontLowerleg" , type = "revolute", position = [0,0,-0.5], jointAxis="-1 0 0")
        pyrosim.Send_Cube(name='FrontLowerleg', pos=[0,0,0] , size=[0.2,0.2,1])

       # pyrosim.Send_Joint( name = "Torso_Head" , parent= "Torso" , child = "Head" , type = "revolute", position = [0,0,1], jointAxis="0 1 0")
        #pyrosim.Send_Cube(name='Backleg', pos=[0,0,0] , size=[0.2,0.4,0.2])
       # pyrosim.Send_Joint( name = "Torso_Leftleg" , parent= "Torso" , child = "Leftleg" , type = "revolute", position = [-0.5, 0, 0], jointAxis="0 1 0.5")
       # pyrosim.Send_Cube(name='Leftleg', pos=[-0.5,0,0] , size=[2,0.2,0.2])
        #pyrosim.Send_Joint( name = "Leftleg_LeftLowerleg" , parent= "Leftleg" , child = "LeftLowerleg" , type = "revolute", position = [-1,0,0], jointAxis="0 1 0")
        #pyrosim.Send_Cube(name='LeftLowerleg', pos=[-2,0,-0.5] , size=[0.1,0.5,0.5])

        #pyrosim.Send_Joint( name = "Torso_Rightleg" , parent= "Torso" , child = "Rightleg" , type = "revolute", position = [0.5, 0, 1], jointAxis="0 1 0.5")
        #pyrosim.Send_Cube(name='Rightleg', pos=[0.5,0,0] , size=[2,0.2,0.2])
        #pyrosim.Send_Joint( name = "Rightleg_RightLowerleg" , parent= "Rightleg" , child = "RightLowerleg" , type = "revolute", position = [1,0,0], jointAxis="0 1 0")
        #pyrosim.Send_Cube(name='RightLowerleg', pos=[2,0,-0.5] , size=[0.1,0.5,0.5])
          
        pyrosim.End()

    def Generate_Brain(self): 
        '''
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

        '''
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "BackLowerleg")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "FrontLowerleg")  
       # pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LeftLowerleg") 
        #pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "RightLowerleg") 
        
        pyrosim.Send_Motor_Neuron(name = 3 , jointName = "Backleg_BackLowerleg")
        pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Frontleg_FrontLowerleg")
        #pyrosim.Send_Motor_Neuron(name = 6 , jointName = "Leftleg_LeftLowerleg")
        #pyrosim.Send_Motor_Neuron(name = 7 , jointName = "Rightleg_RightLowerleg")
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , weight = self.weights[currentRow][currentColumn])

        pyrosim.End()
            




