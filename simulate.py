import constants as c
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
from simulation import SIMULATION
import sys
#Lets Start

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()


'''

backLegSensorValues = numpy.zeros(1000)
FrontLegSensorValues = numpy.zeros(1000)

back_targetAngles = numpy.linspace(0, 2*numpy.pi, 1000)
front_targetAngles = numpy.linspace(0, 2*numpy.pi, 1000)
for i in range(1000):
    back_targetAngles[i] = c.back_amplitude * numpy.sin(c.back_frequency * back_targetAngles[i] + c.back_phaseOffset) 
    front_targetAngles[i]  = c.front_amplitude * numpy.sin(c.front_frequency * front_targetAngles[i] + c.front_phaseOffset) 

#numpy.save('data/back_sins.npy', back_targetAngles, allow_pickle=True, fix_imports=True)
#numpy.save('data/front_sins.npy', front_targetAngles, allow_pickle=True, fix_imports=True)



for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i]= pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    FrontLegSensorValues[i]= pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
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


    time.sleep(1/60)
    print(i)
    #print(i)
numpy.save('data/info.npy', backLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save('data/frontInfo.npy', backLegSensorValues, allow_pickle=True, fix_imports=True)

p.disconnect()  

''' 