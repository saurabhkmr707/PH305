'''from scipy.integrate import dblquad
import numpy as np

def integrand(y, x):
    'y must be the first argument, and x the second.'
    temp = x
    y = x
    x = temp
    return 2.*x*y + 2.*x - x**2. - 2.*y**2 + 72.

ans, err = dblquad(integrand, 0., 8.,
                   lambda x: 0.,
                   lambda x: 6.)
print ans'''

def f(x,y):
	temp = 2.*x*y + 2.*x - x**2. - 2.*y**2 + 72.
	return temp

ay = 0.
by = 6.
ax = 0.
bx = 8.

ny = 2
nx = 2

hy = (by-ay)/(ny)
hx = (bx-ax)/(nx)

s = 0.

for i in range(ny+1):
	if (i ==0 or i == ny):
		p = 1.
	elif (i%2 != 0):
		p = 4.
	else:
		p = 2.
	
	for j in range(nx+1):
		if (j ==0 or j == nx):
			q = 1.
		elif (j%2 != 0):
			q = 4.
		else:
			q = 2.
			
		x = ax + j*hx
		y = ay + i*hy
		s = s + p*q*f(x,y)

ans = hx*hy*s/9.
print ans