

#required libraries
import sys                                 
import ssl
import json
import paho.mqtt.client as mqtt

# for motion sensor
import RPi.GPIO as GPIO
import time
#from datetime import datetime

#called while client tries to establish connection with the server 
def on_connect(mqttc, obj, rc):
    if rc==0:
        print ("Subscriber Connection status code: "+str(rc)+" | Connection status: successful")
        mqttc.subscribe("test" , qos=0)

    elif rc==1:
        print ("Subscriber Connection status code: "+str(rc)+" | Connection status: Connection refused")
        

#called when a topic is successfully subscribed to
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos)+"data"+str(obj))

#called when a message is received by a topic
def on_message(mqttc, obj, msg):
    print("Received message from topic: "+msg.topic+" | QoS: "+str(msg.qos)+" | Data Received: "+str(msg.payload))
    data = str(msg.payload)


    #GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)
    #GPIO.setup(2,GPIO.OUT)

    #if data == "ON":
     #   GPIO.output(2,1)
    #else:
     #   GPIO.output(2,0)
    


#creating a client with client-id=mqtt-test
mqttc = mqtt.Mosquitto()

mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_message = on_message

#Configure network encryption and authentication options. Enables SSL/TLS support.
#adding client-side certificates and enabling tlsv1.2 support as required by aws-iot service
mqttc.tls_set(ca_certs="/etc/mosquitto/ca.crt",
	          certfile="/etc/mosquitto/server.crt",
	          keyfile="/etc/mosquitto/server.key",
              tls_version=ssl.PROTOCOL_TLSv1_2, 
              ciphers=None)
mqttc.username_pw_set("admin", "rajat")

#connecting to aws-account-specific-iot-endpoint
mqttc.connect("192.168.43.176",8883)
mqttc.loop_forever()


    
