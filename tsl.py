import time
import board
import busio
import adafruit_tsl2561

        
class TSL(object):
    
    def __init__(self):
        sensor = self.connect()
        self.leer(sensor)
        
    def connect(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        tsl = adafruit_tsl2561.TSL2561(i2c)
        return tsl
    
    def leer(self, tsl):
        lux = tsl.lux
        self.setLux(lux)
        broad = tsl.broadband
        infra = tsl.infrared
        lumi = tsl.luminosity
    
    def setLux(self, p):
        self.lux = p
    def getLux(self):
        return self.lux
    
    def query(self):
        lux = self.getLux()
        return lux
    
# tsl = TSL()
# lux = tsl.query()
# print (lux)