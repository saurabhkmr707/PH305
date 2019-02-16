a = []
with open('input.txt','r') as f:
	for line in f:
		inner_list = [elt.strip() for elt in line.split( )]
		inner_list = map(float,inner_list)
		a.append(inner_list)

n = len(a)
L = [[0. for x in range(n)] for x in range(n)]
lambd = 1.0
for k in range(0,n-1):
	for i in range(k+1,n):
		lambd = a[i][k]/a[k][k]
		L[i][k] = lambd
		for j in range(0,n+1):
			a[i][j] -= lambd*a[k][j]
			


U = [[0 for x in range(n)] for x in range(n)]
for i in range(n):
	for j in range(n):
		if (i == j):
			L[i][j] = 1.0
		U[i][j] = a[i][j]

#solution

y = [0.0 for x in range(n)]
b = list(y)
for i in range(n):
	b[i] = a[i][-1]
y[0] = b[0]
for i in range(1,n):
	summ = 0
	for j in range(0,i):
		summ += y[j]*a[i][j]
	y[i] = b[i] - summ
X = [0.0 for x in range(n)]
X[n-1] = y[n-1]/U[n-1][n-1]
for i in range(n-2,-1,-1):
	summ = 0.0
	for j in range(i+1,n):
		summ += X[j]*U[i][j]
	X[i] = (y[i]-summ)/U[i][i]
	
print (X)

idmat = [[0.0 for x in range(n)] for x in range(n)]
for i in range(n):
	for j in range(n):
		if (i == j):
			idmat[i][j] = 1.0
			

 

	
