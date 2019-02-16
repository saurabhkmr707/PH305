import math
import matplotlib.pyplot as plt
def euler(x0,xn,interval):
	n = int((int(xn)-int(x0))/interval + 1)

	x = [0.0 for i in range(n)]
	y = [0.0 for i in range(n)]
	x[0] = 0.0
	y[0] = 2.0
	for i in range(1,n):
		x[i] = x[i-1]+interval
	
	for i in range(1,n):
		y[i] = y[i-1] + (4.0*math.exp(0.8*x[i-1]) - 0.5*y[i-1])*interval
	
	return x,y
	
def heuns(x0,xn,interval):
	n = int((int(xn)-int(x0))/interval + 1)

	x = [0.0 for i in range(n)]
	y = [0.0 for i in range(n)]
	x[0] = 0.0
	y[0] = 2.0
	for i in range(1,n):
		x[i] = x[i-1]+interval
	for i in range(1,n):
		phi1 = 4.0*math.exp(0.8*x[i-1]) - 0.5*y[i-1]
		ytemp = y[i-1] + (4.0*math.exp(0.8*x[i-1]) - 0.5*y[i-1])*interval
		
		phi2 = 4.0*math.exp(0.8*x[i]) - 0.5*ytemp
		phi = (phi1+phi2)/2.
		y[i] = y[i-1] + phi*interval
	return x,y

def mid_point(x0,xn,interval):
	n = int((int(xn)-int(x0))/interval + 1)
	x = [0.0 for i in range(n)]
	y = [0.0 for i in range(n)]
	x[0] = 0.0
	y[0] = 2.0
	for i in range(1,n):
		x[i] = x[i-1]+interval
	for i in range(1,n):
		mid = x[i-1] + interval/2.
		ytemp = y[i-1] + (4.0*math.exp(0.8*x[i-1]) - 0.5*y[i-1])*interval/2.
		slope = 4.0*math.exp(0.8*mid) - 0.5*ytemp
		y[i] = y[i-1] + slope*interval
		
	return x,y
def actual(x0,xn,interval):
	n = int((int(xn)-int(x0))/interval + 1)
	x = [0.0 for i in range(n)]
	y = [0.0 for i in range(n)]
	x[0] = 0.0
	y[0] = 2.0
	for i in range(1,n):
		x[i] = x[i-1]+interval
	for i in range(1,n):
		y[i] = (4./1.3)*(math.exp(0.8*x[i])-math.exp(-0.5*x[i])) + 2*math.exp(-0.5*x[i])
	return x,y
	
interval = 0.05
x0 = 0.0
xn = 4.0
x1,y1 = euler(x0,xn,interval)
x2,y2 = heuns(x0,xn,interval)
x3,y3 = mid_point(x0,xn,interval)
x4,y4 = actual(x0,xn,interval)
n = int((int(xn)-int(x0))/interval + 1)
with open('output1.txt','w') as f:
	f.writelines(map("{} {} {} {} {}\n".format,x1,y1,y2,y3,y4))
#plt.plot(x,y)
#plt.show()

