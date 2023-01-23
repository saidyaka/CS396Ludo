import numpy
import constants as c
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random
class SENSOR:
    def __init__(self, name):
        self.linkName = name
        self.values = numpy.zeros(1000)
         
    def Get_Value(self,i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        if i == 1000:
            print(self.values)
  
    def Save_Values(self):
        numpy.save('data/info.npy', self.values, allow_pickle=True, fix_imports=True)
