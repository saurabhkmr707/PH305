import math
import matplotlib.pyplot as plt
def f(x,k):
	x = x+k
	temp = math.exp(-x)*math.sin(x) + math.exp(x)*math.cos(x) + (x**2.)*(math.exp(-x**2.))*math.exp(-x)
	return temp
	

h = 0.08
n = 26
x = [0.0 for i in range(n)]
y = [0.0 for i in range(n)]
#x = [0.0 for i in range(n)]

x[0] = 0.0
y[0] = 0.0


for i in range(1,n):
	x[i] = x[i-1] + h

for i in range(1,n):
	k1 = f(x[i-1],0)
	k2 = f(x[i-1],h/2.)
	k3 = f(x[i-1],h/2.)
	k4 = f(x[i-1],h)
	k = (1./6.)*(k1 + 2.*k2 + 2.*k3 + k4)
	y[i] = y[i-1] + k*h


for i in range(n):
	print y[i]

import matplotlib.pyplot as plt
plt.plot (x,y)
plt.show()



	
