import sys
import serial
import datetime
import csv

ser = serial.Serial('/dev/cu.usbmodem11301',9600) #ポートの情報を記入

while(1):
    value = str(ser.readline().decode('utf-8').rstrip('\n'))
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(date,value)
    with open('Templog.csv', 'a') as f:
        print('{},{}'.format(date,value),file=f)