from servo import Servo
from time import sleep

s1 = Servo(pin=3)  #To be changed according to the pin used
s2 = Servo(pin=0)  #To be changed according to the pin used

s2.move(0)

while True:
#     for i in range(0,150,6):
#         s2.move(i)
#         sleep(0.1)
    s2.move(0)
    sleep(0.3)
    s2.move(195)
    sleep(0.4)

