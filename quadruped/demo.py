import pybullet as p
import numpy as np
import math
import time
from minitaur import Minitaur

physicsClient = p.connect(p.GUI)
p.setGravity(0,0,-10)
minitaur = Minitaur(p)
plane = p.loadURDF("data/plane.urdf")

for i in range (10000):
    p.stepSimulation()
    if i == 0:
        obs = minitaur.GetObservation()
        print(obs)
    random_actions = np.random.rand(8) * math.pi / 4
    random_actions += np.ones(8) * math.pi * 3 / 8
    minitaur.ApplyAction(random_actions)
    # print(minitaur.GetBaseOrientation())
    print(minitaur.GetBasePosition())
    print(minitaur.GetMotorAngles())
    

    time.sleep(1./240.)
