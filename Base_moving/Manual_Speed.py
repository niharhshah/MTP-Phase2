'''
This assumes that forward is just forward with a fixed speed of mspeed (5000)
change the speed in mspeed variable. This variable controls the master speed.

the differential speed (Delta) is used in turn. 
smaller values = slow turn. 

Maximum value of Delta,mspeed = 12000 

for best results 
3000<mspeed<8000
800 < Delta<2000

IMPORTANT: AT ANT TIME 
(Delta + mspeed) <12000
'''

from roboclaw_3 import Roboclaw
from time import sleep
address = 0x80
debug = 0
rc = Roboclaw("COM8",115200)
rc.Open()

#Control Functions
mspeed = 5000
Delta = 1000

#------------------Functions----------------------
# def delay(val=1000):
#     for i in range(0,val):
#         pass

def encoder_test():
    print("This will move robot please confirm we are clear to move")
    if(input("[y/n]").lower()=="y"):
        print("encoder_test")
        #move motor forward for some time
        rc.SetEncM1(address,0)
        rc.SetEncM2(address,0)
        rc.speed(address,64)
        rc.ForwardM2(address,64)
        # delay(d_val)
        sleep(1)
        rc.ForwardM1(address,0)
        rc.ForwardM2(address,0)
        # stop()
        en1=rc.ReadEncM1(address)
        en2=rc.ReadEncM2(address)
        print("forward: enc1={}; enc2={}".format(en1,en2))
        rc.BackwardM1(address,64)
        rc.BackwardM2(address,64)
        # delay(2*d_val)
        sleep(2)
        rc.ForwardM1(address,0)
        rc.ForwardM2(address,0)
        # stop()
        en3=rc.ReadEncM1(address)
        en4=rc.ReadEncM2(address)
        print("backward: enc1={}; enc2={}".format(en3,en4))
        if(en1[1]*en3[1]<0 and en2[1]*en4[1]<0 and en3[1]*en4[1]>0 and en2[1]*en1[1]>0):
            print("encoder test done---working fine")
            return True
        else:
            print("Error in directions of the motor , please reconnect the wires and tune again!!!")
            raise ImportError

def stop():
    rc.ForwardM1(address,0)
    rc.ForwardM2(address,0)
    rc.ForwardMixed(address,0)
    print("stopped")
def connection_test():
    print("This will move robot please confirm we are clear to move")
    if(input("[y/n]").lower()=="y"):
        print("Connection_test")
        rc.SetEncM1(address,0)
        rc.SetEncM2(address,0)
        rc.ForwardM1(address,30)
        sleep(0.5)
        c = rc.ReadEncM1(address)
        if (c[1]> 30 or c[1] < -30):
            print("M1 OK! {}".format(c))    
        rc.ForwardM1(address,0)
        rc.ForwardM2(address,30)
        sleep(0.5)
        c = rc.ReadEncM2(address)
        if (c[1]> 30 or c[1] < -30):
            print("M2 OK! {}".format(c))    
        rc.ForwardM2(address,0)
def Settings():
    global mspeed
    global Delta
    print("The current settings are")
    print("Master Speed: " + str(mspeed))
    print("Delta: "+str(Delta))
    geti = input("C to change and any key to exit ")
    geti = geti.upper()
    if(geti == "C"):
        mspeed_char = input("Enter Master Speed: ")
        mspeed_char = int(mspeed_char)
        mspeed = mspeed_char
        Delta_char = input("Enter Delta: ")
        Delta_char = int(Delta_char)
        Delta = Delta_char
        print("Settings Updated.")
    else:
        print("Nothing to change Exiting ....")
        return
    print("Exiting....")
    return

# Varriables
intSpeed = 0


#----------------Main Function -------------------#
#init functions
# rc.ForwardMixed(address,0)
# rc.TurnLeftMixed(address,0)
# rc.TurnRightMixed(address,0)

#The CLI Interface

print("#########################")
print("Manual Control on jetson nano")
print("please run test to check encoder connection, Case insensitive")
print("F: Forward w master Speed ")
print("B: Backward w master speed  ")
print("L: Left \t R: Right")
print("E: Encoder test")
print("T: Settings")
print("Q or ctrl+c to quit")
# print("Main Battery Voltage is ",rc.ReadMainBatteryVoltage(address)) 
while 1:
    try:
        r_char = input("Please Enter your input: ")
        r_char = r_char.upper()
#------------------Main Functions -----------------------------#            
        if(r_char[0] == "F"):
            rc.SpeedM1M2(address,mspeed,mspeed)            
        if(r_char[0] == "B"):
            intSpeed = -mspeed
            rc.SpeedM1M2(address,intSpeed,intSpeed)
        if(r_char[0] == "E"):
            encoder_test()
        if(r_char[0] == "L"):
            intSpeed = mspeed+Delta
            rc.SpeedM1M2(address,mspeed,intSpeed)
        if(r_char[0] == "R"):
            intSpeed = mspeed+Delta
            rc.SpeedM1M2(address,intSpeed,mspeed)
        if(r_char[0] == "S"):
            stop()
        if(r_char[0] == "C"):
            connection_test()
        if(r_char[0] == "T"):
            Settings()
        if(r_char[0] == "Q"):
            raise KeyboardInterrupt


 #-------------Exception Handling-------------------#   
    except KeyboardInterrupt:
        print("\nExiting....")
        break
    except ValueError:
        print("Speed Missing or Incorrect")
    except AttributeError:
        print("Port Not opened")
    except:
        pass
        # print("Invalid Input")
