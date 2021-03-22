import time
import board
import busio
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
import adafruit_tsl2561


i2c = busio.I2C(board.SCL, board.SDA)
tsl = adafruit_tsl2561.TSL2561(i2c)
        
while True:
    lux = tsl.lux
    broad = tsl.broadband
    infra = tsl.infrared
    lumi = tsl.luminosity
    print(lux)
    time.sleep(2.0)
