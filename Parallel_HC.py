from solution import SOLUTION
import pyrosim.pyrosim as pyrosim
import constants as c
import copy
import os
import shutil
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        print("Deleting")
        os.system("rm brain*.nndf")
        os.system("rm body*.urdf")
        #os.system("rm fitness*.txt")
        os.system(f'touch bestBrain.nndf')
        os.system(f'touch bestBody.urdf')
        self.allTime = 10000
        self.parents = {}
        self.tr = 0
        self.nextAvailableID = 0
        self.maybe = ""
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID+=1
    def Evolve(self):
     
        self.Evaluate(self.parents)
      
      
        for currentGeneration in range(c.numberOfGenerations):

            self.Evolve_For_One_Generation()
    def Evolve_For_One_Generation(self):
        
        self.Spawn()
        
        self.Mutate()
    
        self.Evaluate(self.children)

        self.Print()
        self.Select()

        
    def Evaluate(self, solutions):
        for key in solutions.keys():
            solutions[key].Start_Simulation("DIRECT")
        for key in self.parents:
            solutions[key].Wait_For_Simulation_To_End()

    def Spawn(self):

        self.children = {}
        for index in self.parents:
            self.children[index] = copy.deepcopy(self.parents[index])
            self.children[index].Set_ID(self.nextAvailableID)
            self.nextAvailableID+=1
    

    def Mutate(self):
        for childIndex in self.children:
            self.children[childIndex].Mutate()


    def Select(self):
        for key in self.children:
        
            if self.parents[key].Get_Fitness() > self.children[key].Get_Fitness(): 
                
                self.parents[key] = self.children[key]

    def Print(self):
        best = 1000000000
        besti = 0
        bestr = ''
        i = 0
        for el in self.parents:
            print("Parent: ", self.parents[el].Get_Fitness(), "| Child: ", self.children[el].Get_Fitness())
            pf = self.parents[el].Get_Fitness()
            if pf < best:
            
                best = pf
                besti = self.parents[el].Get_ID()

            
        
        if best < self.allTime:
            self.allTime = best
            self.tr = besti 
            os.system(f'rm bestBrain.nndf')
            os.system(f'rm bestBody.nndf')
            shutil.copyfile(f'brain{self.tr}.nndf', f'tempo.nndf')
            os.rename(f'tempo.nndf', 'bestBrain.nndf')
            shutil.copyfile(f'body{self.tr}.urdf', f'tipo.urdf')
            os.rename(f'tipo.urdf', 'bestBody.urdf')
        print("current " + str(self.allTime))
            

        with open('test5csv','a') as fd:
            fd.write(str(self.allTime)+",")
    def Show_Best(self):      
        print(self.tr)    
        systemCommand = "python3 simulate.py " + "GUI " + str(self.tr) + " 2&>1 &"
        os.system(systemCommand)