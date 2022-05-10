# from roboclaw_3 import Roboclaw
from time import sleep
# address = 0x80
debug = 1
# rc = Roboclaw("\dev\ttyUSB0",115200)
# rc.Open()

odoRead = open("CalibrationFiles/OdemData.txt", "r")
if debug:
    print("file open success!")
lines = odoRead.readlines()
length = len(lines) -1
inter = lines[length].split()
if debug:
    print(int(inter[0]))
    print(int(inter[1]))
M1_enc = int(inter[0])
M2_enc = int(inter[1])
odoRead.close()
odoWrite = open("CalibrationFiles/OdemData.txt", "a")
for i in range(10):
    M1_enc += 10
    M2_enc += 10
    print(M1_enc, M2_enc)
    strng = str(M1_enc) + " " + str(M2_enc) + " 0\n" 
    odoWrite.write(strng)
odoWrite.close()