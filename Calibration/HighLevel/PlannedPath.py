from traceback import print_tb
import serial
import os
from time import sleep
from time import time

#the Important Variables
# Reading the last data not needed as the Arduino is not resetting.
odoWrite = open("mydata.txt", "w")
usb = serial.Serial("/dev/ttyUSB0",115200)
usb.close()
# print("Port closed")
usb.open()
print("Port Opened")
sleep(2) #  Wait for the serial communication to begin
encoders = ""
str_enc = ""
flag = 0
while(1):
    try:
        tr = 7
        t_end = time() + tr
        while(time() < t_end):
            str_enc1 = ""
            str_enc2 = ""
            flag = 0
            usb.write(b"12")
            sleep(0.025)
            usb.write(b"E")
            encoders = usb.read_until()
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
            odoWrite.write(str_enc2 + " "+ str_enc1 +"\n")
        usb.write(b"3333333")
        print("Increased")
        tr = 5
        t_end = time() + tr
        while(time() < t_end):
            str_enc1 = ""
            str_enc2 = ""
            flag = 0
            usb.write(b"12")
            sleep(0.025)
            usb.write(b"E")
            encoders = usb.read_until()
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
            odoWrite.write(str_enc2 + " "+ str_enc1 +"\n")
        usb.write(b"4444444")
        print("Back to normal")
        tr = 7
        t_end = time() + tr
        while(time() < t_end):
            str_enc1 = ""
            str_enc2 = ""
            flag = 0
            usb.write(b"12")
            sleep(0.025)
            usb.write(b"E")
            encoders = usb.read_until()
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
            odoWrite.write(str_enc2 + " "+ str_enc1 +"\n")
        usb.write(b"3333333")
        print("increased Speed")
        tr = 5
        t_end = time() + tr
        while(time() < t_end):
            str_enc1 = ""
            str_enc2 = ""
            flag = 0
            usb.write(b"12")
            sleep(0.025)
            usb.write(b"E")
            encoders = usb.read_until()
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
            odoWrite.write(str_enc2 + " "+ str_enc1 +"\n")
        raise KeyboardInterrupt
    except KeyboardInterrupt:
        str_enc1 = ""
        str_enc2 = ""
        flag = 0
        usb.write(b"8")
        sleep(0.01)
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
        print("Saving The file...")
        print(str_enc2 + " "+ str_enc1 +"\n")
        odoWrite.write(str_enc2 + " "+ str_enc1 + "\n")
        break
    except:
        pass    
# odoWrite.write(str(M2_encr) + " "+ str(M1_encr) + " 1" + str(pic_no+1)+"\n")
odoWrite.close()
usb.close()
exit()
