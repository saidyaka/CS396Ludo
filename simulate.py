import pybullet as p
import time
#Lets Start
physicsClient = p.connect(p.GUI)
p.loadSDF("box.sdf")
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)
p.disconnect()

