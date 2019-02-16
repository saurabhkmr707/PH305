x0 = 13.
a1 = 26.
c1 = 12.
m1 = 10001.

x00 = 48.
a11 = 16.
c11 = 87.
m11 = 10001.
circle = 0
square = 0
p1 = []
p2 = []
#x = [i for i in range(3000)]
for i in range(3000):
	x1 = (a1*x0+c1)%m1
	x0 = x1
	x = x0/10001.
	
	x11 = (a11*x00+c11)%m11
	x00 = x11
	y = x00/10001.
	
	if (x*x + y*y < 1.):
		circle += 1.
	square += 1.
	p1.append(4.*(circle/square))
	
print (4.*(circle/square))

import random
import math
random.seed(9001)

cir = 0

sq = 3000

temp = 0.
for i in range(0, sq):

	x2 = random.random()**2.
	y2 = random.random()**2.
	
	if math.sqrt(x2 + y2) <= 1.0:
		cir += 1
	temp += 1.
	p2.append(4.*float(cir)/temp)


pi = (float(cir) / sq) * 4.


print(pi)
import matplotlib.pyplot as plt
plt.plot(p2)
plt.show()


	
