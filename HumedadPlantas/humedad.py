import time
import board
import busio
import math
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

porcentaje0 = (chan0.voltage-4.094)/(-2.738/100)
porcentaje1 = (chan1.voltage-4.094)/(-2.746/100)

print("{:>5}\t{:>5}".format('Porcentaje0', 'Porcentaje1'))

#while True:
print("{:>5}\t{:>14}".format(math.floor(porcentaje0), math.floor(porcentaje1)))
time.sleep(0.5)
