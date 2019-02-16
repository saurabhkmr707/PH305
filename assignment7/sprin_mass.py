import math
def euler(x0,xn,interval):
	n = int((int(xn)-int(x0))/interval + 1)

	t = [0.0 for i in range(n)]
	v = [0.0 for i in range(n)]
	x = [0.0 for i in range(n)]
	t[0] = 0.0
	v[0] = 0.0
	x[0] = 1.0
	for i in range(1,n):
		t[i] = t[i-1]+interval
	
	for i in range(1,n):
		v[i] = v[i-1] - x[i-1]*interval
		x[i] = x[i-1] + v[i-1]*interval
		
 	return x,t

def heuns(x0,xn,interval):
	n = int((int(xn)-int(x0))/interval + 1)

	x = [0.0 for i in range(n)]
	t = [0.0 for i in range(n)]
	v = [0.0 for i in range(n)]
	x[0] = 1.0
	v[0] = 0.0
	t[0] = 0.0
	for i in range(1,n):
		t[i] = t[i-1]+interval
	for i in range(1,n):
		phi1 = -x[i-1]
		xtemp = x[i-1] + v[i-1]*interval
		phi2 = -xtemp
		phi = (phi1+phi2)/2.
		v[i] = v[i-1] + phi*interval
		
		phi1 = v[i-1]
		vtemp = v[i-1] - x[i-1]*interval
		phi2 = vtemp
		phi = (phi1+phi2)/2.
		#print phi
		x[i] = x[i-1] + phi*interval
		#print x[i]
	return x,t

def mid_point(x0,xn,interval):
	n = int((int(xn)-int(x0))/interval + 1)
	x = [0.0 for i in range(n)]
	v = [0.0 for i in range(n)]
	t = [0.0 for i in range(n)]
	x[0] = 1.0
	v[0] = 0.0
	t[0] = 0.0
	for i in range(1,n):
		t[i] = t[i-1]+interval
	for i in range(1,n):
		mid = t[i-1] + interval/2.
		xtemp = x[i-1] + v[i-1]*interval/2.
		slope = -xtemp
		v[i] = v[i-1] + slope*interval
		
		vtemp = v[i-1] - x[i-1]*interval/2.
		slope = vtemp
		x[i] = x[i-1] + slope*interval
		
	return x,t
	
def actual(x0,xn,interval):
	n = int((int(xn)-int(x0))/interval + 1)
	x = [0.0 for i in range(n)]
	v = [0.0 for i in range(n)]
	t = [0.0 for i in range(n)]
	x[0] = 1.0
	v[0] = 0.0
	t[0] = 0.0
	for i in range(1,n):
		t[i] = t[i-1]+interval
	for i in range(n):
		x[i] = math.cos(t[i])
	return x,t


interval = 0.01
t0 = 0.0
tn = 400.0
x1,t1 = euler(t0,tn,interval)
x2,t2 = heuns(t0,tn,interval)
x3,t3 = mid_point(t0,tn,interval)
x4,t4 = actual(t0,tn,interval)
n = int((int(tn)-int(t0))/interval + 1)
with open('output.txt','w') as f:
	f.writelines(map("{} {} {} {} {}\n".format,t1,x1,x2,x3,x4))
#plt.plot(t,x)
#plt.show()
