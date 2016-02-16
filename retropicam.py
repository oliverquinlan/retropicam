#RetroPiCam - A Gif tweeting camera for a Box Brownie by Oliver Quinlan


#setup libraries
from gpiozero import LED, Button, Buzzer
from time import sleep
from picamera import PiCamera
from datetime import datetime
import os

#variables
length = 8
resolution = "640, 480"

#Twython setup
### You will need to setup a twitter app on twitter.com and get the authentication details to make this work
import sys
from twython import Twython
CONSUMER_KEY = 'xxx'
CONSUMER_SECRET = 'xxx'
ACCESS_KEY = 'xxx'
ACCESS_SECRET = 'xxx'
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#setup ins and outs
btn = Button(23)
led = LED(17)
bz = Buzzer(2)

#setup camera

#camera = PiCamera()
#camera.resolution = (320, 240)

#Setect button
while True:
    if btn.is_pressed:
        #User feedback
        led.blink(0.05,0.05)
        bz.beep(on_time=0.1,off_time=0.1)
        print("Button pressed, taking "+length+" photos...")
        #Take photos
        filename = "/home/pi/retropicam/photos/image"+"-"+str(datetime.now()) 
        #Take high res photo
        camera = PiCamera()
        camera.resolution = (1280, 960)
        camera.capture("/home/pi/retropicam/photos/archive/"+filename+".jpg")
        #Take gif photos
        camera.resolution = (320, 240)
        for num in range (length):
          camera.capture(filename+"-"+str(num)+".jpg")      
        #User feedback
        print("Photos Taken")
        led.off()
        bz.off()
        #makegif
        print("Making gif...")
        os.system("gm convert -delay 15 /home/pi/retropicam/photos/*.jpg /home/pi/retropicam/photos/gif.gif")
        gifsave = "mv gif.gif /home/pi/retrocam/photos/archive/"+filename+".gif"
        os.system(gifsave)
        #Tidy up
        os.system("rm /home/pi/retropicam/photos/*.jpg")
        #tweetgif
        print("Tweeting gif...")
        photo = open('/home/pi/retropicam/photos/gif.gif','rb')
        api.update_status_with_media(media=photo, status='A new Retrocam photo...')
        #User feedback
        print("Photo Tweeted!")
        bz.on()
        sleep(0.5)
        bz.off()
    else:
        #User Feedback
        print("Ready to take pictures")
        led.on()
        bz.off()
