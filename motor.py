

import numpy
import constants as c
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random

class MOTOR:
    def __init__(self, name):
        self.jointName = name
        #self.values = motorValues


    def Set_Value(self, desiredAngle, robotId):
        pyrosim.Set_Motor_For_Joint(
                bodyIndex = robotId,
                jointName = self.jointName,
                controlMode = p.POSITION_CONTROL,  
                targetPosition = desiredAngle,
                maxForce = 100)
    
        