from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/aaronhmiller/picow-ota/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "ota_updater.py")
ota_updater.download_and_install_update_if_available()
