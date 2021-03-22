import time
import board
import adafruit_dht
import RPi.GPIO as GPIO

dhtDevice = adafruit_dht.DHT22(board.D4)
pin = 21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.LOW)

i = 0
while i < 1:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
     
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    
    reference = 21.7 
    if temperature_c <= reference:
        GPIO.output(pin, GPIO.HIGH)
    if temperature_c > reference:
        GPIO.output(pin, GPIO.LOW)
    dhtDevice.exit()
    time.sleep(10.0)
    
    i = i+1


GPIO.output(pin, GPIO.LOW)
GPIO.cleanup

    

    