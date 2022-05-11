import numpy as np
import matplotlib.pyplot as plt
from roboclaw_3 import Roboclaw
from time import sleep
rc = Roboclaw("COM5",115200)
rc.Open()
address = 0x80
debug = 1
rc.SetM2VelocityPID(address,2.1173,0.26858,0,52562)
rc.SetM1VelocityPID(address,2.03045,0.2444,0,54812)
pwr = np.array([i for i in range (126)])
print (pwr)
sped = np.zeros(pwr.shape)
cur = 0
speed = 0
#give robot power
rc.BackwardM2(address,0)
sleep(1)
for i in range(len(pwr)):
    dspeed = int(pwr[i])
    print("current_speed", dspeed)
    print(rc.BackwardM2(address,int(pwr[i])))
    # print(rc.ReadPWMs(address))
    cur = rc.ReadSpeedM1(address)
    sped[i] = cur[1]
    sleep(0.1)
rc.ForwardM2(address,0)
print(pwr.shape,sped.shape)
plt.plot(pwr,sped)
plt.title ("M2 Velocity Vs PWM")
plt.xlabel("PWM")
plt.ylabel("Velocity")
plt.show()
# plt.savefig("M2.png")