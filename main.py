from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
firmware_url = "https://raw.githubusercontent.com/aaronhmiller/picow-ota/"
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
ota_updater.download_and_install_update_if_available()

from machine import Pin, Timer
led = machine.Pin("LED", machine.Pin.OUT)

def tick(timer):
    led.toggle()

Timer().init(freq=20, callback=tick) # call tick twice a sec
