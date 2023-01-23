import constants as c
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
class ROBOT:
    def __init__(self):
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain.nndf")
    def Prepare_To_Sense(self):
        self.sensors ={}
        for linkName in pyrosim.linkNamesToIndices:
           self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for name in self.sensors:
            self.sensors[name].Get_Value(t)
    def Think(self):
        self.nn.Update()
        self.nn.Print()
        
    def Prepare_To_Act(self):
        self.joints ={}
        for jointName in pyrosim.jointNamesToIndices:
           self.joints[jointName] = MOTOR(jointName)
           '''
                self.amplitude = c.front_amplitude
                self.frequency = c.front_frequency
                self.offset = c.front_phaseOffset
                
                self.targetAngles = numpy.sin(self.frequency*numpy.linspace(0, 2*numpy.pi, 10000)+self.offset)*self.amplitude   

            '''
      
    def ACT(self, i):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                print(jointName.encode("utf-8"))
                self.joints[jointName.encode("utf-8")].Set_Value(desiredAngle, self.robotId)
