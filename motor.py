

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
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
            if self.jointName == b'Torso_FrontLeg':
            
                self.amplitude = c.front_amplitude
                self.frequency = c.front_frequency
                self.Offset = c.front_phaseOffset
            else:
                self.amplitude = c.back_amplitude
                self.frequency = c.back_frequency
                self.Offset = c.back_phaseOffset

            self.values = numpy.sin(self.frequency*numpy.linspace(0, 2*numpy.pi, c.steps)+self.Offset)*self.amplitude
    def Set_Value(self,robotId, i):
        pyrosim.Set_Motor_For_Joint(
                bodyIndex = robotId,
                jointName = self.jointName,
                controlMode = p.POSITION_CONTROL,  
                targetPosition = self.values[i],
                maxForce = 100)
        
      


    def Save_Values(self):
        numpy.save('data/motifyo.npy', self.values, allow_pickle=True, fix_imports=True)
        