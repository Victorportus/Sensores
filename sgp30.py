import time
import board
import busio
import adafruit_sgp30

class SGP30(object):
    
    def __init__(self):
        sensor = self.connect()
        while True:
            self.read(sensor)
            data = self.dic()
            print(data)
        
    def connect(self):
        i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
        sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
        sgp30.iaq_init()        
        sgp30.set_iaq_baseline(38815, 39046)
        return sgp30
    
    def read(self, s):
        eco2= 400
        tvoc= 0
        count = 0
        while eco2==400 and tvoc==0:
            time.sleep(1)
            eco2 = s.eCO2
            tvoc = s.TVOC
#             print(eco2, tvoc)
            self.setEco2(eco2)
            self.setTvoc(tvoc)
            count += 1
            if count > 10:
                count = 0
                s.set_iaq_baseline(38815, 39046)
                
    def dic(self):
        dic = {'ECO2' : self.getEco2(), 'TVOC' : self.getTvoc()}
        return dic
        
    def getEco2(self):
        return self.eco2
    def setEco2(self, p):
        self.eco2 = p
        
    def getTvoc(self):
        return self.tvoc
    def setTvoc(self, p):
        self.tvoc = p
        
sgp = SGP30()        

