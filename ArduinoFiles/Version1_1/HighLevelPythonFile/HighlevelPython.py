import serial
from time import sleep

# try:
usb = serial.Serial("/dev/ttyUSB0",9600)
# usb.write(b"1")
usb.close()
print("Port closed")
usb.open()
print("Port Opened")
sleep(0.5)
# except:
#     print("Please Connect USB device default address is /dev/ttyUSB0")
#     exit()
i = 0
encoders = ""
try:
    while True:
        usb.write(b"12")
        sleep(0.1)
        usb.write(b"S")
        encoders = usb.read_until()
        print(encoders)
except:
    
    usb.write(b"8")
    usb.close()