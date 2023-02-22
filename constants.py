
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random



numberOfGenerations = 100


populationSize = 1
steps = 1000

numSensorNeurons = 13
numMotorNeurons = 12
motorJointRange = 1

numLinks = 20
initPosition = [0, 0, 3]
