from sds011 import *
import time
sensor = SDS011("/dev/ttyUSB0")
sensor.sleep(sleep=False)
time.sleep(10.0)

pmt_2_5, pmt_10 = sensor.query()
print(time.strftime("%m/%d/%y"), time.strftime("%H:%M"), end='')
print(f"    PMT2.5: {pmt_2_5} µg/m3    ", end='')
print(f"PMT10: {pmt_10} µg/m3")
sensor.sleep(sleep=True)
time.sleep(2)



