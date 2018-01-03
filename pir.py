import RPi.GPIO as GPIO
import time
import smtplib
import os
import paho.mqtt.client as mqtt
import ssl
import sys

from gpiozero import MotionSensor
server =smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("nehaliacharya1@gmail.com", "kosginehu1110")
msg="Intrusion possible"
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN, GPIO.PUD_DOWN)  #Read output from PIR motion sensor
GPIO.setup(2,GPIO.OUT) #LED output pin
#i=GPIO.input(4)
intru='mosquitto_pub -h 192.168.43.176 -u admin -P rajat -p 8883 -t test -m 0 --cafile /etc/mosquitto/ca.crt --cert /etc/mosquitto/client.crt --key /etc/mosquitto/client.key'
nonintru='mosquitto_pub -h 192.168.43.176 -u admin -P rajat -p 8883 -t test -m 1 --cafile /etc/mosquitto/ca.crt --cert /etc/mosquitto/client.crt --key /etc/mosquitto/client.key'
while True:
    time.sleep(1)
    i=GPIO.input(4)
    if i==0:
        os.system(intru)
	GPIO.output(2,0) #Turn off LED
	time.sleep(1)
    elif i==1: #when output from motion sensor is high
	GPIO.output(2,1) #turn on LED
        server.sendmail("nehaliacharya1@gmail.com","rajat.kachhwaha@gmail.com",msg)
        os.system(nonintru)
	time.sleep(1)
#os.system(intru)
server.quit()
