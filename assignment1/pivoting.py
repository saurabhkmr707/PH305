def row_swap(matrix,a,b):
	temp = matrix
	temp[a] = matrix[b]
	temp[b] = matrix[a]
	return temp
	
def pivoting(a,n):
	for j in range(n):
		mx = 0.
		for i in range(j,n):
			if (abs(a[i][j]) > mx):
				mx = a[i][j]
				idxi = i 
		a = row_swap(a,idxi,j)
	return a
		


def gaussian(a,n):
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

a = [[3.0,-0.1,-0.2,7.85],[0.1,7.0,-0.3,-19.3],[0.3,-0.2,10.0,71.4]]
#[1,1,1]]

a_pivoted = pivoting(a,len(a))
print (gaussian(a_pivoted,len(a_pivoted)))
		 
