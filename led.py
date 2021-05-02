import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

import time

pin = int(input("Que led desea prender?  "))

def prender(p):
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, GPIO.HIGH)
    GPIO.output(p, GPIO.HIGH)
    
def apagar(p):
    GPIO.output(p, GPIO.LOW)

prender(pin)
time.sleep(2.0)
apagar(pin)

