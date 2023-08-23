
import math,datetime

v=[]

cas1= datetime.datetime.now()
for n in range (20000000):
    v.append(math.sin(n))

cas2 = datetime.datetime.now()

print((cas2-cas1).total_seconds())