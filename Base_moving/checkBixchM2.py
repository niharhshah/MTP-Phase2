from cv2 import readOpticalFlow
from roboclaw_3 import Roboclaw
from time import sleep

rc = Roboclaw("COM8",115200)
rc.Open()
address = 128
try:
    while True:
        rc.BackwardM1(address,120)
        rc.BackwardM2(address,120)
        sleep(0.5)
        print(rc.ReadPWMs(address))
        sleep(0.5)
        rc.BackwardM1(address,0)
        rc.BackwardM2(address,0)
        sleep(1)
except:
    rc.BackwardM1(address,0)
    rc.BackwardM2(address,0)
        