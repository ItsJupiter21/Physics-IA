from time import time
numbers=[0]
n=1
nlast=0
i=0
iter=265000

ts=time()

while i<=(iter-2)/2:
    i+=1
    n+=nlast
    nlast+=n

tf=time()
dt=tf-ts
print(dt)
