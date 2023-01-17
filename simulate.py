import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
#Lets Start
back_amplitude = numpy.pi/2
back_frequency = 25
back_phaseOffset = -numpy.pi/2
#front
front_amplitude = numpy.pi/2
front_frequency = 25
front_phaseOffset = -numpy.pi/2

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
FrontLegSensorValues = numpy.zeros(1000)

back_targetAngles = numpy.linspace(0, 2*numpy.pi, 1000)
front_targetAngles = numpy.linspace(0, 2*numpy.pi, 1000)
for i in range(1000):
    back_targetAngles[i] = back_amplitude * numpy.sin(back_frequency * back_targetAngles[i] + back_phaseOffset) 
    front_targetAngles[i]  = front_amplitude * numpy.sin(front_frequency * front_targetAngles[i] + front_phaseOffset) 

numpy.save('data/back_sins.npy', back_targetAngles, allow_pickle=True, fix_imports=True)
numpy.save('data/front_sins.npy', front_targetAngles, allow_pickle=True, fix_imports=True)



for i in range(1000):
    p.stepSimulation()
   # backLegSensorValues[i]= pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    #FrontLegSensorValues[i]= pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
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

