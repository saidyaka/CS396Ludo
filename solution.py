import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c
import random
class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
       
        self.linksWithSensors = []
        self.numSensorNeurons = 0
        self.numMotorNeurons = 0
        self.numlinks =  int(random.uniform(3, 15))

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
    def Generate_Link(self,  linkNumber, sensor ,position, length, width, height):
        if sensor: 
            self.linksWithSensors.append(linkNumber)
        x, y, z = position
        pyrosim.Send_Cube(name=f'link{linkNumber}', pos=[x,y,z] , size=[length,width,height], sensor = sensor)



    def Generate_Joints(self, axis, prevAxis, linkNumber, length, width, height, position):

            if axis =='x':
                if linkNumber == 0 or prevAxis == None:
                    pyrosim.Send_Joint( name = f'link{linkNumber}_link{linkNumber+1}' , parent= f'link{linkNumber}' , child = f'link{linkNumber+1}' , type = "revolute", position = [length/2, 0, position[2]], jointAxis="1 0 0")
                elif linkNumber != self.numlinks-1:
                    if prevAxis == 'y':
                        pyrosim.Send_Joint( name = f'link{linkNumber}_link{linkNumber+1}' , parent= f'link{linkNumber}' , child = f'link{linkNumber+1}' , type = "revolute", position = [-length/2, -width/2, 0], jointAxis="1 0 0")
                    elif prevAxis == 'z':
                        pyrosim.Send_Joint( name = f'link{linkNumber}_link{linkNumber+1}' , parent= f'link{linkNumber}' , child = f'link{linkNumber+1}' , type = "revolute", position = [-length/2, 0, -height/2], jointAxis="1 0 0")
                    else:
                        pyrosim.Send_Joint( name = f'link{linkNumber}_link{linkNumber+1}' , parent= f'link{linkNumber}' , child = f'link{linkNumber+1}' , type = "revolute", position = [-length, 0, 0], jointAxis="1 0 0")
                else:
                    return
            if axis == 'y':
                if linkNumber == 0:
                    pyrosim.Send_Joint( name = f'link{linkNumber}_link{linkNumber+1}' , parent= f'link{linkNumber}' , child = f'link{linkNumber+1}' , type = "revolute", position = [0, -length/2, position[2]], jointAxis="0 1 0")
                elif linkNumber != self.numlinks-1:
                    if prevAxis == 'x':
                        pyrosim.Send_Joint( name = f'link{linkNumber}_link{linkNumber+1}' , parent= f'link{linkNumber}' , child = f'link{linkNumber+1}' , type = "revolute", position = [-length/2, -width/2, 0], jointAxis="0 1 0")
                    elif prevAxis == 'z':
                        pyrosim.Send_Joint( name = f'link{linkNumber}_link{linkNumber+1}' , parent= f'link{linkNumber}' , child = f'link{linkNumber+1}' , type = "revolute", position = [0, -length/2, -height/2], jointAxis="0 1 0")
                    else:                    
                        pyrosim.Send_Joint( name = f'link{linkNumber}_link{linkNumber+1}' , parent= f'link{linkNumber}' , child = f'link{linkNumber+1}' , type = "revolute", position = [0, -length, 0], jointAxis="0 1 0")
                else:
                    return
            if axis ==  'z':
                if linkNumber == 0:
                    pyrosim.Send_Joint( name = f'link{linkNumber}_link{linkNumber+1}' , parent= f'link{linkNumber}' , child = f'link{linkNumber+1}' , type = "revolute", position = [0, 0, position[2]-length/2], jointAxis="0 0 1") # rotate around x/z plane 010
                elif linkNumber != self.numlinks-1:
                    if prevAxis == 'x':
                        pyrosim.Send_Joint( name = f'link{linkNumber}_link{linkNumber+1}' , parent= f'link{linkNumber}' , child = f'link{linkNumber+1}' , type = "revolute", position = [-length/2, 0, -height/2], jointAxis="0 0 1")
                    elif prevAxis == 'y':
                        pyrosim.Send_Joint( name = f'link{linkNumber}_link{linkNumber+1}' , parent= f'link{linkNumber}' , child = f'link{linkNumber+1}' , type = "revolute", position = [0, -width/2, -height/2], jointAxis="0 0 1")
                    else:
                        pyrosim.Send_Joint( name = f'link{linkNumber}_link{linkNumber+1}' , parent= f'link{linkNumber}' , child = f'link{linkNumber+1}' , type = "revolute", position = [0, 0, -height], jointAxis="0 0 1")
                else:
                    return
    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        

        position = c.initPosition
        axis = None
        t = int(random.uniform(3, 9))
        print(t)
        for i in range(self.numlinks):
            print(i)
            length, width, height = random.uniform(0.1, 0.9), random.uniform(0.1, 0.9),random.uniform(0.1, 0.9)
            self.Generate_Link(i, random.choice([True, True, False]),
                            position= position,
                            length= length,
                            width= width,
                            height= height)

            prevAxis = axis
            axis = random.choice(['x', 'y', 'z'])

            self.Generate_Joints(axis, prevAxis, i, length, width, height, position)

            if axis == 'x':
                 position = [length/2, 0, 0]
            if axis ==  'y':
                position = [0, width/2, 0]
            if axis == 'z':
                position = [0, 0, height/2]
        
        pyrosim.End()
        self.numSensorNeurons = len(self.linksWithSensors)
        self.numMotorNeurons = self.numlinks - 1
        self.weights = numpy.random.rand(self.numSensorNeurons, self.numMotorNeurons) * 2 - 1

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork(f'brain{self.myID}.nndf')
        for i in range(self.numSensorNeurons):
            pyrosim.Send_Sensor_Neuron(name = i , linkName = f"link{self.linksWithSensors[i]}")
        
        for i in range(self.numlinks, 2*self.numlinks):
            linkNumber = i - self.numlinks
            if linkNumber != self.numlinks-1:
                pyrosim.Send_Motor_Neuron(name = linkNumber + self.numSensorNeurons , jointName = f"link{linkNumber}_link{linkNumber+1}")

        for currentRow in range(self.numSensorNeurons):
            for currentColumn in range(self.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + self.numSensorNeurons  , weight = self.weights[currentRow, currentColumn])
        pyrosim.End()
            




