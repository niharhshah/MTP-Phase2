import serial
import os
from time import sleep
from time import time

odoWrite = open("my_data", "w")
usb = serial.Serial("/dev/ttyUSB0",115200)
usb.close()
print("Port closed")
usb.open()
print("Port Opened")
sleep(0.2) #  Wait for the serial communication to begin
encoders = ""
str_enc1 = ""
str_enc2 = ""
try:
    usb.write(b"12")
    while 1:
        usb.write(b"E")
        encoders = usb.read_until()
        sleep(0.025)
        for i in encoders:
            if((i>= 48 and i < 58)or i == 32):
                if(i == 32):
                    flag = 1
                else:
                    if flag:
                        str_enc1 += str(i-48)
                    else:
                        str_enc2 += str(i-48)
        # M1_encr = int(str_enc1) + M1_enc
        # M2_encr = int(str_enc2) + M2_enc
        print(str_enc2,"\t",str_enc1)
        odoWrite.write(str_enc2 + " "+ str_enc1 + "\n")
except:
    usb.write(b"8")
    usb.close()
    odoWrite.close()
print("All done! Have a good day!")