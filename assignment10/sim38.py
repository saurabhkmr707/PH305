def f(x,y):
	temp = 2.*x*y + 2.*x - x**2. - 2.*y**2 + 72.
	return temp

ay = 0.
by = 6.
ax = 0.
bx = 8.

ny = 6
nx = 6

hy = (by-ay)/(1.*ny)
hx = (bx-ax)/(1.*nx)

s = 0.

for i in range(ny+1):
	if (i ==0 or i == ny):
		p = 1.
	elif (i%3 == 0):
		p = 2.
	else:
		p = 3.
	
	for j in range(nx+1):
		if (j ==0 or j == nx):
			q = 1.
		elif(j%3 == 0):
			q = 2.
		else:
			q = 3.
			
		x = ax + j*hx
		y = ay + i*hy
		s = s + p*q*f(x,y)

ans = hx*hy*s*(9./64.)
print ans/48.
