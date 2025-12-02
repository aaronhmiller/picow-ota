from machine import Pin, Timer
from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/aaronhmiller/picow-ota/main"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
ota_updater.download_and_install_update_if_available()

led = Pin(16, Pin.OUT)

def tick(timer):
    led.toggle()

Timer().init(freq=2, callback=tick) # call tick twice a sec