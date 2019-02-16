from math import *
def f(x):
	temp = exp(-x)*sin(x) + exp(x)*cos(x) + (x**2.)*(exp(-x**2.))*exp(-x)
	return temp

#ay = 0.
#by = 6.
ax = 0.
bx = 2.

#ny = 2
nx = 12

#hy = (by-ay)/(ny)
hx = (bx-ax)/(nx)

s = 0.


for j in range(nx+1):
	if (j ==0 or j == nx):
		q = 1.
	elif (j%2 != 0):
		q = 4.
	else:
		q = 2.
		
	x = ax + j*hx
	#y = ay + i*hy
	s = s + q*f(x)

ans = hx*s/3.
print ans
