from solution import SOLUTION
import pyrosim.pyrosim as pyrosim
import constants as c
import copy
import os
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
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
            solutions[key].Start_Simulation("GUI")
        
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
        print()
        for el in self.parents:
            print("Parent: ", self.parents[el].Get_Fitness(), "| Child: ", self.children[el].Get_Fitness())
        print()
    
    def Show_Best(self):
        best_parent_key = "None"
        best_fitness = 1000000
        for key in self.parents:
            parent_fitness = self.parents[key].Get_Fitness()
            if parent_fitness < best_fitness:
                best_fitness = parent_fitness
                best_parent_key = key

        self.parents[best_parent_key].Start_Simulation("GUI")
        print("Best fitness: ", best_fitness)
        #self.parent.Evaluate("GUI")