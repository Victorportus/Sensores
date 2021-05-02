import time
import board
import busio
import math
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import interruptor

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)
interruptor.prender(21)
x=chan0.voltage
porcentaje0 = (chan0.voltage-3.1520961943418686)/(-2.758084170049135/100)
#porcentaje1 = (chan1.voltage-4.094)/(-2.746/100)
#print(chan0.voltage)
#print(chan1.voltage)

print("{:>5}".format('Porcentaje0'))

#while True:
print("{:>5}".format(math.floor(porcentaje0)))
interruptor.apagar(21)
