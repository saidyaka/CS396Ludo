import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c
class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
       
        self.linksWithSensors = []
        self.numSensorNeurons = 0
        self.numMotorNeurons = 0


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
        pyrosim.End()
    def Generate_Link(self, shape, linkNumber, sensor ,position, length, width, height):
        if sensor: 
            self.linksWithSensors.append(linkNumber)
        x, y, z = position
        if shape == 'cube':
            pyrosim.Send_Cube(name=f'link{linkNumber}', pos=[x,y,z] , size=[length,width,height], sensor = sensor)
        elif shape == 'cylinder':
            pyrosim.Send_Cylinder(name=f'link{linkNumber}', pos=[x,y,z] , length=length, radius=width, sensor = sensor)
        elif shape == 'sphere':
            pyrosim.Send_Sphere(name=f'link{linkNumber}', pos=[x,y,z] , radius=length , sensor = sensor)
        else:
            return 'Invalid shape'

        if linkNumber == 0:
            pyrosim.Send_Joint( name = f'link{linkNumber}_link{linkNumber+1}' , parent= f'link{linkNumber}' , child = f'link{linkNumber+1}' , type = "revolute", position = [-c.length/2, 0, c.height], jointAxis="0 0 1")
        elif linkNumber != c.numLinks-1:
            pyrosim.Send_Joint( name = f'link{linkNumber}_link{linkNumber+1}' , parent= f'link{linkNumber}' , child = f'link{linkNumber+1}' , type = "revolute", position = [-length, 0, 0], jointAxis="0 0 1")
        else:
            return
    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        
        pyrosim.Send_Cube(name='Head', pos=c.initPosition , size=[c.length,c.width,c.height])
        # pyrosim.Send_Sphere(name='Head', pos=c.initPosition , radius=c.length)
        pyrosim.Send_Joint( name = 'Head_link0' , parent= 'Head' , child = 'link0' , type = "revolute", position = [-2, 0, 1], jointAxis="0 0 1")
        position = c.initPosition
        length, width, height = c.length, c.width, c.height
        for i in range(c.numLinks):
            length, width, height = random.uniform(1, 2), random.uniform(1, 2), random.uniform(1, 2)
            position = [-length/2, 0, 0]
            self.Generate_Link(random.choice(c.linkShapes), 
                            i, random.choice([0,1]),position,
                            length= length,
                            width= width,
                            height= height)
        pyrosim.End()
        self.numSensorNeurons = len(self.linksWithSensors)
        self.numMotorNeurons = c.numLinks - 1
        self.weights = numpy.random.rand(self.numSensorNeurons, self.numMotorNeurons) * 2 - 1

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork(f'brain{self.myID}.nndf')
        for i in range(self.numSensorNeurons):
            pyrosim.Send_Sensor_Neuron(name = i , linkName = f"link{self.linksWithSensors[i]}")
        
        for i in range(c.numLinks, 2*c.numLinks):
            linkNumber = i - c.numLinks
            if linkNumber != c.numLinks-1:
                pyrosim.Send_Motor_Neuron(name = linkNumber + self.numSensorNeurons , jointName = f"link{linkNumber}_link{linkNumber+1}")

        for currentRow in range(self.numSensorNeurons):
            for currentColumn in range(self.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + self.numSensorNeurons  , weight = self.weights[currentRow, currentColumn])
        pyrosim.End()
            




