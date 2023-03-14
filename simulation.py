from world import WORLD
from robot import ROBOT
import constants as c
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

class SIMULATION:
    def __init__(self,directOrGUI, solutionID, show):
        self.directOrGUI = directOrGUI

        self.runType = directOrGUI
        if self.runType == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)


        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
    
        print(show)

        self.world = WORLD()
        self.robot = ROBOT(solutionID, show)


    def Run(self):
        for i in range(c.steps):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.ACT(i)

            if self.runType == "GUI":
                time.sleep(1/100000)
            '''
         
            pyrosim.Set_Motor_For_Joint(
                bodyIndex = robotId,
                jointName = b'Torso_BackLeg',
                controlMode = p.POSITION_CONTROL,  
                targetPosition = back_targetAngles[i],
                maxForce = 100)
            pyrosim.Set_Motor_For_Joint(
                bodyIndex = robotId,
                jointName = b'Torso_FrontLeg',
                controlMode = p.POSITION_CONTROL,  
                targetPosition = front_targetAngles[i],
                maxForce = 100)

'''
        #self.Get_Fitness()
    def Get_Fitness(self):
        self.robot.Get_Fitness()
    def __del__(self):
        p.disconnect()
   




