
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random



numberOfGenerations = 40

populationSize = 5
steps = 10000

numSensorNeurons = 13
numMotorNeurons = 12
motorJointRange = 1

numLinks = 20
linkShapes = ['cube']
initPosition = [0, 0, 5]
