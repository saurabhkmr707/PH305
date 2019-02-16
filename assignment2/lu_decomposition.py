import copy
def lu_decomp(a,n):
	a1 = copy.deepcopy(a)
	lambd = 1.0
	L1 = [[0. for i in range(n)] for i in range(n)]
	for i in range(n):
		for j in range(n):
			if (i == j):
				L1[i][j] = 1.0
	for k in range(0,n-1):
		for i in range(k+1,n):
			lambd = a1[i][k]/a1[k][k]
			L1[i][k] = lambd
			for j in range(n+1):
				a1[i][j] -= lambd*a1[k][j]
	U1 = [[0. for i in range(n)] for i in range(n)]
	for i in range(n):
		for j in range(n):
			U1[i][j] = a1[i][j]
	return L1,U1

def solving_for_y(L,b):
	L2 = copy.deepcopy(L)
	b1 = copy.deepcopy(b)
	n = len(L2)
	
	y1 = [0. for i in range(n)]
	
	y1[0] = b1[0]
	for k in range(1,n):
		sum_ly = 0.
		for j in range(0,k):
			sum_ly += L2[k][j]*y1[j]
		y1[k] = b1[k] - sum_ly
	
	return y1

def solving_for_x(U,y):
	U2 = copy.deepcopy(U)
	y2 = copy.deepcopy(y)
	n = len(U2)
	x2 = [0. for i in range(n)]
	x2[n-1] = y2[n-1]/U2[n-1][n-1]
	for k in range(n-2,-1,-1):
		sum_ax = 0.0
		for j in range(k+1,n):
			sum_ax += U2[k][j]*x2[j]
		x2[k] = (y2[k] - sum_ax)/U2[k][k]
	return x2

def transpose(lst):
    newlist = []
    i = 0
    while i < len(lst):
        j = 0
        colvec = []
        while j < len(lst):
            colvec.append(lst[j][i])
            j = j + 1
        newlist.append(colvec)
        i = i + 1
    return newlist

def inverse(a):
	a3 = copy.deepcopy(a)
	n = len(a3)
	L3,U3 = lu_decomp(a3,n)
	
	
	temp_a3 = list(a3)
	a3 = [[0.0 for i in range(n)] for j in range(n)]
	for i in range(n):
		for j in range(n):
			a3[i][j] = temp_a3[i][j]
	a_inv1 = []
	temp_y = []
	
	#creating the identity matrix
	id_mat = [[0. for i in range(n)] for j in range(n)]
	for i in range(n):
		for j in range(n):
			if (i == j):
				id_mat[i][j] = 1.
		
	for i in range(n):
		temp_col = list(id_mat[i])
		y11 = list(solving_for_y(L3,temp_col))
		temp_y.append(y11)

	
	for i in range(n):
		temp_x = list(solving_for_x(U3,temp_y[i]))
		a_inv1.append(temp_x)	

	
	temp_ainv = list(a_inv1)
	for i in range(n):
		for j in range(i):
			temp = a_inv1[i][j]
			a_inv1[i][j] = a_inv1[j][i]
			a_inv1[j][i] = temp
	#a_inv1 = transpose(temp_ainv)
	return a_inv1
			
	

#a = [[3.0,-0.1,-0.2,7.85],[0.1,7.0,-0.3,-19.3],[0.3,-0.2,10.0,71.4]]
a = []
with open('input.txt','r') as f:
	for line in f:
		inner_list = [elt.strip() for elt in line.split( )]
		inner_list = map(float,inner_list)
		a.append(inner_list)
	
#a = [[8,1.,6,15],[3,5,7,15],[4,9,2,15]]
L,U = lu_decomp(a,3)
n = len(a)
b = [0. for i in range(n)]

for i in range(n):
		b[i] = a[i][n]

y = solving_for_y(L,b)
x = solving_for_x(U,y)
a_inv = inverse(a)
print ("This is the lower triangular matrix:\n")
for i in range(len(L)):
	print (L[i])
print ("____________________________________")
print ("")
print ("This is the upper traingular matrix:\n")
for i in range(len(U)):
	print (U[i])
print ("")
print (solving_for_y(L,b))
#xx = np.matmul(L,U)
#print (xx)
print (x)
for i in range(len(a_inv)):
	print (a_inv[i])
