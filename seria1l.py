import os
import sys
import serial
from serial import Serial
import time

comport = str(sys.argv[1])
port = int(sys.argv[2])

s = serial.Serial(comport, baudrate = port, timeout = 1)
time.sleep(3)
n = 10
dl = [0]*n
dFile = open('data.txt', 'w')

def getValues():
    
    s.write(b'g')
    arduinoData = s.readline().decode().split('\r\n')
    
    return arduinoData[0]

    
while(1):

    userInput = input('Get data points?')

    if userInput == 'y':
        for i in range(0,n):
            data = getValues()
            dFile.write(data + ' ')
            data = int(data)
            dl[i] = data
            
        da = sum(dl)/n
        print(da)
        print(dl)

        dFile.close()
        break