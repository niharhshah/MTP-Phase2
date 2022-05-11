from datetime import datetime
now = datetime.now()

odoRead = open("CalibrationFiles/OdemData.txt", "r")
lines = odoRead.readlines()
length = len(lines) -1
inter = lines[length].split()
# print(inter)
M1_enc = int(inter[1])
M2_enc = int(inter[2])
odoRead.close()
odoWrite = open("CalibrationFiles/OdemData.txt", "a")
strng = now.strftime("%H%M%S%f") +" "+str(M1_enc) + " " + str(M2_enc) + " 1\n" 
odoWrite.write(strng)
odoWrite.close()
