import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 

class interruptor(object):
    
    def __init__(self):
        self.prender()
        self.apagar()
        
    def prender(p):
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.HIGH)
        GPIO.output(p, GPIO.HIGH)
    
    def apagar(p):
        GPIO.output(p, GPIO.LOW)


interruptor.prender(9)

#interruptor.apagar(9)