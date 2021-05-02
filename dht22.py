import time
import board
import adafruit_dht
import RPi.GPIO as GPIO
import sys

class DHT22(object):
    
    def __init__(self):
        sensor = self.connect()
        self.read(sensor)
        
        
    def connect(self):
        GPIO.setmode(GPIO.BCM)
        dhtDevice = adafruit_dht.DHT22(board.D17)
        return dhtDevice
    
    def read(self, dht):
        i = 0
        while i < 2:
            try:
                self.setTemp(dht.temperature)
                self.setHumi(dht.humidity)
                dht.exit()
                break
            except RuntimeError as error:
                i += 1
                time.sleep(2.0)
                continue
        if i >= 2:
            dht.exit()
            sys.exit()
        
    def setHumi(self, p):
        self.humi = p
    def getHumi(self):
        return self.humi
    
    def setTemp(self, p):
        self.temp = p
    def getTemp(self):
        return self.temp
    
    def query(self):
        temp = self.getTemp()
        humi = self.getHumi()
        return temp, humi
            
dht = DHT22()
temp, humi = dht.query()
print (temp, humi)