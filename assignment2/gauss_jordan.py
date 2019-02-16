import copy
def inverse(a,n):
	temp_a = list(a)
	a = [[0. for i in range(n)] for i in range(n)]
	
	for i in range(n):
		for j in range(n):
			a[i][j] = temp_a[i][j]
	
	a_inv = [[0. for i in range(n)] for i in range (n)]
	
	for i in range(n):  
		for j in range(n):
			if (i == j):
				a_inv[i][j] = 1.0
				
	lambd = 1.0
	for k in range(0,n-1):
		for i in range(k+1,n):
			lambd = a[i][k]/a[k][k]
			for j in range(n):
				a[i][j] -= lambd*a[k][j]
				a_inv[i][j] -= lambd*a_inv[k][j]
	
	for k in range(n-1,0,-1):
		lambd = 1.0
		for i in range(k-1,-1,-1):
			lambd = a[i][k]/a[k][k]
			for j in range(n):
				a[i][j] -= lambd*a[k][j]
				a_inv[i][j] -= lambd*a_inv[k][j]
				
	for i in range(n):
		temp = a[i][i]
		for j in range(n):
			a[i][j] = a[i][j]/temp
			a_inv[i][j] = a_inv[i][j]/temp
	
	return a,a_inv
	
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
		


def gauss_jordan(a,n):
	a1 = copy.deepcopy(a)
	lambd = 1.0
	for k in range(0,n-1):
		for i in range(k+1,n):
			lambd = a1[i][k]/a1[k][k]
			for j in range(n+1):
				a1[i][j] -= lambd*a1[k][j]
	
	for k in range(n-1,0,-1):
		lambd = 1.0
		for i in range(k-1,-1,-1):
			lambd = a1[i][k]/a1[k][k]
			for j in range(n+1):
				a1[i][j] -= lambd*a1[k][j]
	
	for i in range(n):
		temp = a1[i][i]
		for j in range(n+1):
			a1[i][j] = a1[i][j]/temp
	
	
	x = [0 for i in range(n)]
	for i in range(n):
		x[i] = a1[i][n]
	return a1,x


				
				
				 
a = [[3.0,-0.1,-0.2,7.85],[0.1,7.0,-0.3,-19.3],[0.3,-0.2,10.0,71.4]]
#a = []
'''with open('input.txt','r') as f:
	for line in f:
		inner_list = [elt.strip() for elt in line.split( )]
		inner_list = map(float,inner_list)
		a.append(inner_list)
		'''

print ("The input matrix is:\n")
for i in range(len(a)):
	print (a[i])
print ("")
print ("__________________________\n")



a_output = pivoting(a,len(a))
a_output,x1 = gauss_jordan(a,len(a))

print ("The output matrix is:\n")

for i in range(len(a_output)):
	print (a_output[i])
print ("")
print ("__________________________\n")

	
print ("")
print ("The solution to these equations is:")
print (x1)
print ("")


xx1,inv_a = inverse(a,3)
print ("The inverse of matrix A is:\n")
for i in range(len(inv_a)):
	print (inv_a[i])

print ("")



		 
