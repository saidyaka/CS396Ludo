
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random



numberOfGenerations = 1


populationSize = 1
steps = 1000

numSensorNeurons = 13
numMotorNeurons = 12
motorJointRange = 1

numLinks = 10
linkShapes = ['cube', 'sphere', 'cylinder']
initPosition = [0, 0, 1]
length, width, height =1, 1, 1