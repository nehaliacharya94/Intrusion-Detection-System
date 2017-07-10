# Intrusion Detection System 
_(Fall: September 2016 - December 2016)_

I designed an **Intrusion Detection System** for security purposes. The project aimed at developing a prototype that could provide a layer of 
security against intruders and it could also be managed easily by the owner of the system. 

The following devices and tools were used for successful implementation of the project:
* Raspberry Pi 
* Passive Infrared Motion Sensor (PIR) - to detect motion of an object and is connected to the GPIO ports of Raspberry Pi via the 
breadboard
* USB web camera - for live video streaming of the area being monitored
* LED - to glow if motion is detected 
* Python - programming language used 
* MQTT protocol, SSL/TLS, Mosquitto - for providing security to the system
>
The set up is shown below. 
>
<img width="407" alt="capture" src="https://user-images.githubusercontent.com/29523536/28005030-69cc59a2-6516-11e7-8ac4-7140446afc08.PNG">

When there is motion in an area being monitored, it is detected by the PIR motion sensor that causes the led to glow and a value of __“1”__ is 
outputted to the Raspberry Pi terminal and an email is sent to the user to notify that there might have been an intrusion. 
Similarly, when there is no movement, a value of __“0”__ is outputted to the terminal. If the user is suspicious of this activity and 
wishes to know who the person is, he/she can open the web browser and plug in the IP address of the Raspberry Pi to which the USB 
web camera is connected. The user can then remotely access the system to check who intruded into the place with the help of the web camera 
that records and live streams the video.
>
<img width="402" alt="pic1" src="https://user-images.githubusercontent.com/29523536/28005307-e2e792d8-6517-11e7-9b5f-779a568fb1c5.PNG">

Data that is generated in the form of 0′s and 1′s is published to the MQTT broker. Every device that is subscribed to this topic will 
receive the data published by the broker to them. Topic is created by the publisher which is then published via a secure channel built by 
the broker.

To provide security to the system, I used a light-weight protocol, Message Queuing Telemetry Transport Protocol __(MQTT)__ that uses a 
publish-subscribe pattern. MQTT allows for __SSL__ communication on __port__ __8883__ that provides __network__ __encryption__.
>
<img width="406" alt="pic2" src="https://user-images.githubusercontent.com/29523536/28005394-4a6027f4-6518-11e7-8fc0-9a721a9a7a80.PNG">

So any device that needs access to the broker needs to provide a __username__ and __password__ to authenticate themselves. We ensure that the 
username and password is sent over an encrypted network to protect them against man in the middle attacks. The network is encrypted 
using client side and server side certificates.
