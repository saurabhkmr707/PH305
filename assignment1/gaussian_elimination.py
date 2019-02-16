def gaussian(a):
	n = len(a)
	lambd = 1.0
	for k in range(0,n-1):
		for i in range(k+1,n):
			lambd = a[i][k]/a[k][k]
			for j in range(k,n+1):
				a[i][j] -= lambd*a[k][j]
				
	x = [0 for i in range(n)]
	x[n-1] = a[n-1][n]/a[n-1][n-1]
	#print x[n-1]
	for k in range(n-2,-1,-1):
		sum_ax = 0.0
		for j in range(k+1,n):
			sum_ax += a[k][j]*x[j]
		x[k] = (a[k][n] - sum_ax)/a[k][k]
	return x

a = [[2,1,3,4],
[2,-2,-1,1],
[-2,4,1,1]]

print (gaussian(a,3))
		 
