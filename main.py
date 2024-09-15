

#iav2x.csv have the LED at full brigthness fuck me
from machine import Pin,PWM,I2C
from time import sleep, time_ns
import rp2,ws2812

from servo import Servo
import tsl2561

ledsm = rp2.StateMachine(0, ws2812.ws2812, freq=8_000_000, sideset_base=Pin(16))
ledsm.active(1)

brightness=1

ttystart=False

Led = PWM(Pin(28), freq=600000,invert=True)
def LedB(B):
    Led.duty_u16(int(65535*B))

def ledw(r,g,b):
    r=round(r*brightness)
    g=round(g*brightness)
    b=round(b*brightness)
    ledsm.put((g<<24) | (r<<16) | (b<<8))

Servo = Servo(pin=29,)    

i2c = I2C(1, sda=Pin(14), scl=Pin(15))
sensor = tsl2561.TSL2561(i2c)
sensor.integration_time(402)
sensor.gain(16)#16 is the most sensitive
#1:3918.05 max
#16:247.0598 max


times=[]


Servo.move(0)
ledw(0,0,255)

if ttystart==1:
    input("Press enter to start")#wait for tty to start
else:
    while(rp2.bootsel_button()==0):
        continue
    sleep(10)
tRef0=time_ns()

ledw(0,0,0)
for q in range(2):#amount of itterations
    
    index=open('index.txt','a+')
    try:
        char=int(index.read())
    except:
        char=0
    index.close()
    index=open('index.txt','w')
    index.write(str(char+1))
    index.close()
    char=str(char)
    file=open("on"+str(char)+'.csv','w')

    Servo.move(180)
    sleep(0.5)
    Servo.move(0)
    sleep(0.5)


    tRef=time_ns()
    for f in range(0,191,2):
        A=f

        Servo.move(0)
        file.flush()
        sleep(f/800)
        Servo.move(A)
        sleep(f/300+0.05)
        print(A)
        for i in range(0,21,1):
            B=i/20
            LedB(B)
            sleep(0.02)
            for i in range(4):
                L=sensor.read()#no autogain, calibrated out
            
                out=[B,L,A]
                print(B,L) 
                file.write(','.join(map(str, out))+'\n')
            
        LedB(0)
            
            
    t= 0.000000001*(time_ns()-tRef)

    print(t)
    times.append(t)
    file.close()


t0= 0.000000001*(time_ns()-tRef0)
print(tdef)
print(times)
Servo.move(0)
ledw(255,0,0)
while(1):
    ledw(255,0,0)
    sleep(0.5)
    ledw(0,0,255)
    sleep(0.5)