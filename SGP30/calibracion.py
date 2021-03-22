import time
import board
import busio
import adafruit_sgp30
 
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

 
# Create library object on our I2C port
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

 
print("SGP30 serial #", [hex(i) for i in sgp30.serial])

sgp30.iaq_init()
co2eq_base, tvoc_base = sgp30.get_iaq_baseline()
print (sgp30.get_iaq_baseline())


 
elapsed_sec = 0
  
while True:
    print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))
    time.sleep(1)
    elapsed_sec += 1
    if elapsed_sec > 10:
        elapsed_sec = 0
        print(sgp30.get_iaq_baseline())