import math
import matplotlib.pyplot as plt
pi = math.pi
T = 2.*pi
h = 0.02*T
n = 510
t = [0.0 for i in range(n)]
v = [0.0 for i in range(n)]
x = [0.0 for i in range(n)]

t[0] = 0.0
v[0] = 0.0
x[0] = 1.0

for i in range(1,n):
	t[i] = t[i-1] + h

for i in range(1,n):
	v[i] = v[i-1] - x[i-1]*h
	x[i] = x[i-1] + v[i-1]*h
	
for i in range(len(t)):
	t[i] = t[i]/T
E = [0]*n
for i in range(n):
	E[i] = 0.5*(x[i]**2. + v[i]**2.)
plt.plot(x,v)
#plt.yticks([float(i)*0.1 for i in range(-15,20,5)])
plt.show()
