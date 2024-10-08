
# https://micropython-tsl2561.readthedocs.io/en/latest/tsl2561.html
import tsl2561
from machine import I2C, Pin,PWM
i2c = I2C(1, sda=Pin(14), scl=Pin(15))
sensor = tsl2561.TSL2561(i2c)

Led = PWM(Pin(28), freq=600000,invert=True)
def LedB(B):
    Led.duty_u16(int(65535*B))

LedB(1)
sensor.gain(16)#16 is the most sensitive

#1:3918.05 max
#16:247.0598 max

vmax=0

while 1:
#     BB,IR=sensor.read(0,1)#no autogain, but raw
    L=sensor.read()#no autogain, calibrated out

        
#     print(BB,IR)
    print(L)
        
        
            