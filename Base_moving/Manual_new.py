from roboclaw_3 import Roboclaw
from time import sleep
address = 0x80
debug = 0
rc = Roboclaw("COM8",115200)
rc.Open()

#------------------Functions----------------------
# def delay(val=1000):
#     for i in range(0,val):
#         pass
	 
def ForwardFunction(speed):
    if(speed > 127 or speed < 0):
        raise ValueError
    # rc.ForwardM1(address,speed)
    # rc.ForwardM2(address,speed)
    rc.BackwardMixed(address,speed)
    print("forward w speed " + str(speed))
def BackwardFunction(speed):
    if(speed > 127 or speed < 0):
        raise ValueError
    # rc.BackwardM1(address,speed)
    # rc.BackwardM2(address,speed)
    rc.ForwardMixed(address,speed)
    print("Back w speed " + str(speed))
def encoder_test():
    print("This will move robot please confirm we are clear to move")
    if(input("[y/n]").lower()=="y"):
        print("encoder_test")
        #move motor forward for some time
        rc.SetEncM1(address,0)
        rc.SetEncM2(address,0)
        rc.ForwardM1(address,64)
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
            raise ValueError

def left(speed):
    if(speed > 127 or speed < 0):
        raise ValueError
    rc.TurnLeftMixed(address,speed)
    print("Left")
def right(speed):
    if(speed > 127 or speed < 0):
        raise ValueError
    rc.TurnRightMixed(address,speed)
    print("Right")
def stop():
    # rc.ForwardM1(address,0)
    # rc.ForwardM2(address,0)
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
speed = 0
#----------------Main Function -------------------#
# rc.SetM1VelocityPID(address,3.34744,0.31924,0.0,12750.0)
# rc.SetM2VelocityPID(address,3.57856,0.30318,0.0,13500.0)
rc.SetM1VelocityPID(address,2.35410,0.28226,0,12000)
rc.SetM2VelocityPID(address,2.35410,0.25502,0,13687)
rc.ForwardMixed(address,0)
rc.TurnLeftMixed(address,0)
rc.TurnRightMixed(address,0)

print("#########################")
print("Manual Control on jetson nano")
print("please run test to check encoder connection, Case insensitive")
print("Fxxx: Forward w speed xxx ")
print("Bxxx: Backward w speed xxx ")
print("L: Left \t R: Right")
print("E: Encoder test")
print("Main Battery Voltage is ",rc.ReadMainBatteryVoltage(address)) 
while 1:
    try:
        r_char = input("Please Enter your input: ")
        r_char = r_char.upper()
        if (debug == 1):
            print("Raw_input time = " +  str(r_char[0]))
            print("Raw_input variable = " + str(r_char[1:]))
#------------------Main Functions -----------------------------#            
        if(r_char[0] == "F"):
            speed = int(r_char[1:])
            ForwardFunction(speed)
        if(r_char[0] == "B"):
            speed = int(r_char[1:])
            BackwardFunction(speed)
        if(r_char[0] == "E"):
            encoder_test()
        if(r_char[0] == "L"):
            speed = int(r_char[1:])
            left(speed)
        if(r_char[0] == "R"):
            speed = int(r_char[1:])
            right(speed)
        if(r_char[0] == "S"):
            stop()
        if(r_char[0] == "C"):
            connection_test()
 #-------------Exception Handling-------------------#   
    except KeyboardInterrupt:
        print("\nExiting....")
        break
    except ValueError:
        print("Speed Missing or Incorrect")
    except AttributeError:
        print("Port Not opened")
    except:
        print("Invalid Input")
