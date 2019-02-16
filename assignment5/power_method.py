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
	
	return a_inv

def power(a):
	n = len(a)
	eigvec = [1./3. for x in range(n)]
	prev_eig = 0.0
	while (True):
		eigtemp = []
		for i in range(n):
			summ = 0.0
			for j in range(len(a[0])):
				summ += a[i][j]*eigvec[j]
			eigtemp.append(summ)
		maxm = max(eigtemp)
		minm = min(eigtemp)
		maxm_ind = eigtemp.index(maxm)
		if (abs(minm) > abs(maxm)):
			maxm_ind = eigtemp.index(minm)
		maxm = max(abs(maxm),abs(minm))
	
		eig = eigtemp[maxm_ind]

		if (abs(abs(eig)-abs(prev_eig))/abs(eig) < 0.00000001):
			break

		prev_eig = eig
		for i in range(n):
			eigtemp[i] = eigtemp[i]/eig
		eigvec = list(eigtemp)
	return eig,eigvec


mat1 = []
with open('inp1.txt','r') as f:
	for line in f:
		inner = [x for x in line.split()]
		inner = map(float,inner)
		mat1.append(inner)


mat1_inv = inverse(mat1,len(mat1))
mat3 = [[0.0 for x in range(10)] for x in range(10)]
for i in range(len(mat3)):
	for j in range(len(mat3)):
		if (i == j):
			mat3[i][j] = 4.0
			if (i+1 < len(mat3[0])):
				mat3[i+1][j] = 2.0
			if (i+2 < len(mat3[0])):
				mat3[i+2][j] = 1.0
			if (i-1 >= 0):
				mat3[i-1][j] = 2.0
			if (i-2 >= 0):
				mat3[i-2][j] = 1.0

'''for i in range(len(mat3)):
	print (mat3[i])
print ("")'''
mat3_inv = inverse(mat3,len(mat3))
eigenvalue,eigenvector = power(mat3_inv)

print eigenvector
print 1./eigenvalue 	


