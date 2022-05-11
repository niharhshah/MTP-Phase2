from roboclaw_3 import Roboclaw
from datetime import datetime
address = 0x80
debug = 0
rc = Roboclaw("\dev\ttyUSB0",115200)
rc.Open()
now = datetime.now()

odoRead = open("CalibrationFiles/OdemData.txt", "r")
if debug:
    print("file open success!")
lines = odoRead.readlines()
length = len(lines) -1
inter = lines[length].split()
if debug:
    print(int(inter[1]))
    print(int(inter[2]))
M1_enc = int(inter[1])
M2_enc = int(inter[2])
rc.SetEncM1(address,M1_enc)
rc.SetEncM2(address,M2_enc)
odoRead.close()
odoWrite = open("CalibrationFiles/OdemData.txt", "a")
for i in range(50):
    rc.SpeedM1M2(address,4000,3000)
    M1_enc = rc.ReadEncM1(address)
    M2_enc = rc.ReadEncM2(address)
    sleep(0.02)
    if debug:
        print(M1_enc, M2_enc)
    strng = now.strftime("%Y%m%d%H%M%S%f") +" "+str(M1_enc) + " " + str(M2_enc) + " 0\n" 
    odoWrite.write(strng)
odoWrite.close()