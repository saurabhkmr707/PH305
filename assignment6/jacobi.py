a = []
with open("input2.txt",'r') as f:
	for line in f:
		inner = [x for x in line.split()]
		inner = map(float,inner)
		a.append(inner)
n = len(a)
flag = True
count = 0
c = 0.
d = 0.
d = [[0 for x in range(n)] for x in range(n)]

for i in range(n):
	for j in range(n):
		d[i][j] = a[i][j]

while(True):
	count = count+1
	maxm = 0
	p = 0
	q = 0
	for i in range(n):
		for k in range(i+1,n):
			if (abs(a[i][k]) >= maxm):
				maxm = abs(a[i][k])
				p = i
				q = k
	
	if (maxm < 0.00001):
		break
	
	theta = (a[q][q] - a[p][p])/(2*a[p][q])
	t = 1.0/(abs(theta) + (theta**2 + 1)**0.5)
	if (theta < 0):
		t = -t
	#print ('tehta ',theta)
	#print ('t ',t)
	c = 1.0/((t**2. +1.)**0.5)
	#print ('c ',c)
	s = c*t;
	#print ('s ',s)
	d[p][q] = 0
	d[q][p]	= 0
	#print ('apq ',a[p][q])
	d[p][p] = (c**2)*a[p][p] + (s**2)*a[q][q] - 2*c*s*a[p][q]
	#print d[p][p]
	d[q][q] = (s**2.)*a[p][p] + (c**2.)*a[q][q] + 2.*c*s*a[p][q]
	for j in range(n):
		if (j != p) and (j != q):
			d[j][p] = c*a[j][p] - s*a[j][q]
			d[p][j] = d[j][p]
			d[j][q] = c*a[j][q] + s*a[j][p]
			d[q][j] = d[j][q]
	for i in range(n):
		for j in range(n):
			a[i][j] = d[i][j]

for i in range(n):
	print a[i]
print count

