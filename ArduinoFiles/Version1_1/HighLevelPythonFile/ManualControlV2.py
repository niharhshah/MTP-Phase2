import serial
from time import sleep
# import sys
odoRead = open("demoFile.txt", "r")
# odoRead = open("CalibrationFiles/OdemData.txt", "r")
# if debug:
#     print("file open success!")
lines = odoRead.readlines()
length = len(lines) -1
inter = lines[length].split()
# if debug:
#     print(int(inter[1]))
#     print(int(inter[2]))
M2_enc = int(inter[0])
M1_enc = int(inter[1])
pic_no = int(inter[3])
print(M2_enc,M1_enc,pic_no)
odoRead.close()
# exit()
# try:
odoWrite = open("demoFile.txt", "a")
usb = serial.Serial("/dev/ttyUSB0",9600)
# usb.write(b"1")
usb.close()
print("Port closed")
usb.open()
print("Port Opened")
sleep(0.5) #  Wait for the serial communication to begin
# except:
#     print("Please Connect USB device default address is /dev/ttyUSB0")
#     exit()
encoders = ""
str_enc = ""
flag = 0
while True:
    try:
        str_enc1 = ""
        str_enc2 = ""
        flag = 0
        M1_encr = 0;
        M2_encr = 0;
        usb.write(b"12")
        sleep(0.1)
        usb.write(b"E")
        encoders = usb.read_until()
        # print(encoders)
        for i in encoders:
            if((i>= 48 and i < 58)or i == 32):
                if(i == 32):
                    flag = 1
                else:
                    if flag:
                        str_enc1 += str(i-48)
                    else:
                        str_enc2 += str(i-48)
        M1_encr = int(str_enc1) + M1_enc
        M2_encr = int(str_enc2) + M2_enc
        print(str(M2_encr),"\t",int(M1_encr))
        odoWrite.write(str(M2_encr) + " "+ str(M1_encr) + " 0 " + str(pic_no)+"\n")
    # except PortNotOpenError:
    #     print("Port Not open Error!")
    #     exit()
    except KeyboardInterrupt:
        print("exiting")
        odoWrite.close()
        usb.write(b"8")
        usb.close()
        break
exit()
