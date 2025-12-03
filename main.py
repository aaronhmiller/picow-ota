from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
firmware_url = "https://raw.githubusercontent.com/aaronhmiller/picow-ota/"
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
ota_updater.download_and_install_update_if_available()

from machine import Pin, Timer
import time
led = machine.Pin("LED", machine.Pin.OUT)

def dot():
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.1)

def dash():
    led.on()
    time.sleep(0.3)
    led.off()
    time.sleep(0.1)
   
def beat(timer):
    dot(); dot(); dot(); dash() #5th symphony-like?
    time.sleep(0.5) #pause between calls

def taeb(timer):
    dash(); dash(); dash(); dot()
    time.sleep(0.5) #pause
    
def tick(timer):
    led.toggle()

Timer().init(freq=2, callback=taeb) # call twice a sec 
