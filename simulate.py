import pybullet as p
import time
#Lets Start
physicsClient = p.connect(p.GUI)
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)
p.disconnect()

