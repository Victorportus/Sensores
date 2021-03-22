import time
import board
import busio
import math
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

chan2 = AnalogIn(ads, ADS.P2)

polu = chan2.value

if 0 <= polu & polu <= 3199:
    print ("Aire fresco")
if 3200 <= polu & polu <= 4799:
    print ("Baja polucion")
if 4800 <= polu & polu <= 6399:
    print ("Polucion media")
if 6400 <= polu & polu <= 11199:
    print ("Polucion alta")
if polu >= 11200:
    print ("Polucion muy alta")
