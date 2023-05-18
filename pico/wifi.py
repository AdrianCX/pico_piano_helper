import network
import socket
import time
import re
import config
import machine

def wait_wlan(wlan):
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(1)

    if wlan.status() != 3:
        print("Failed setting up wifi, will restart in 30 seconds")
        time.sleep(30)
        machine.reset()

def setup_ap():
    wlan = network.WLAN(network.AP_IF)
    wlan.config(essid=config.WIFI_SSID, password=config.WIFI_PASSWORD) 
    wlan.active(True)
    wait_wlan(wlan)
    
    print('set up access point:', config.WIFI_SSID, 'with ip = ', wlan.ifconfig()[0])
    return wlan

def connect_wlan():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    wlan.disconnect()
    
    wlan.active(True)
    wlan.connect(config.WIFI_SSID, config.WIFI_PASSWORD)

    wait_wlan(wlan)
    
    print('connected to wifi:', config.WIFI_SSID, 'with ip = ', wlan.ifconfig()[0])
    return wlan

def run():
    wlan = connect_wlan() if not config.WIFI_AP_MODE else setup_ap()
