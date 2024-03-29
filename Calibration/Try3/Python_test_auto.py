import serial
import os
from time import sleep
from time import time
from numpy.random import randint

#the Important Variables
iterations = 200

def capture(pee):
    os.system("rs-save-to-disk")
    os.rename("rs-save-to-disk-output-Depth.png","Depth-"+str(pee)+".png")
    os.rename("rs-save-to-disk-output-Color.png",str(pee)+".png")

def finallly():
    os.system("rm *.csv")
    os.system("mv Depth-* CalibrationFiles/Depth/")
    os.system("mv *.png CalibrationFiles/Color/")

def random_time():
    tr = randint(40,101)
    return tr/100
# Setup. 
os.system("echo \"0 0 1 0\" > CalibrationFiles/OdemData.txt")
# Reading the last data not needed as the Arduino is not resetting.
odoWrite = open("CalibrationFiles/OdemData.txt", "a")
usb = serial.Serial("/dev/ttyUSB0",115200)
usb.close()
print("Port closed")
usb.open()
print("Port Opened")
sleep(0.2) #  Wait for the serial communication to begin
curr_iteration = 0
capture(curr_iteration)
encoders = ""
str_enc = ""
flag = 0
while(curr_iteration < iterations):
    tr = random_time()
    print(curr_iteration,tr)
    t_end = time() + tr
    try:
        while(time() < t_end):
            str_enc1 = ""
            str_enc2 = ""
            flag = 0
            M1_encr = 0
            M2_encr = 0
            usb.write(b"9")
            sleep(0.025)
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
            # M1_encr = int(str_enc1) + M1_enc
            # M2_encr = int(str_enc2) + M2_enc
            print(str_enc2,"\t",str_enc1)
            odoWrite.write(str_enc2 + " "+ str_enc1 + " 0 " + str(curr_iteration)+"\n")
        raise KeyboardInterrupt
    except KeyboardInterrupt:
        str_enc1 = ""
        str_enc2 = ""
        flag = 0
        curr_iteration += 1
        print("Capturing")
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
        # odoWrite.write(str(M2_encr) + " "+ str(M1_encr) + " 1 " + str(curr_iteration)+"\n")
        print(str_enc2 + " "+ str_enc1 + " 1 " + str(curr_iteration)+"\n")
        odoWrite.write(str_enc2 + " "+ str_enc1 + " 1 " + str(curr_iteration)+"\n")
        capture(curr_iteration)
        # break
    except:
        pass    
# odoWrite.write(str(M2_encr) + " "+ str(M1_encr) + " 1" + str(pic_no+1)+"\n")
finallly()
odoWrite.close()
usb.close()
exit()
