
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random



numberOfGenerations = 10
back_amplitude = numpy.pi/2
back_frequency = 5
back_phaseOffset = -numpy.pi/2

populationSize = 10
steps = 1000
front_amplitude = numpy.pi/2
front_frequency = 10
front_phaseOffset = -numpy.pi/2