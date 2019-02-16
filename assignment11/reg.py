import math
def fn(x,a0,a1):
	return a0*(1.-math.exp(-a1*x))

def df_a0(x,a1):
	return (1-math.exp(-a1*x))

def df_a1(x,a0,a1):
	return a0*x*math.exp(-a1*x)

def transpose(lst):
	result = [[0. for x in range(len(lst))] for x in range(len(lst[0]))]
	for i in range(len(lst)):
		for j in range(len(lst[0])):
			result[j][i] = lst[i][j]
	return result

def matmul(l1,l2):
	result = [[0. for x in range(len(l2[0]))] for x in range(len(l1))]
	for i in range(len(l1)):
		for j in range(len(l2[0])):
			for k in range(len(l2)):
				result[i][j] += l1[i][k] * l2[k][j]
	return result

def inverse(a):
	n = len(a)
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
		    
a = []
with open('inp1.txt', 'r') as f:
	for line in f:
		inner = [x for x in line.split()]
		inner = map(float,inner)
		a.append(inner)
n = len(a)
y = []
x = []
A = [1. for i in range(2)]
for i in range(len(a)):
	y.append(a[i][1])
	x.append(a[i][0])
for k in range(10):
	D = []
	for i in range(n):
		temp = []
		temp.append(y[i] - fn(x[i],A[0],A[1]))
		D.append(temp)

	Z = []
	for i in range(n):
		zi = []
		zi.append(df_a0(x[i],A[1]))
		zi.append(df_a1(x[i],A[0],A[1]))
		Z.append(zi)

	Zt = transpose(Z)
	ZZt = matmul(Zt,Z)
	Zinv = inverse(ZZt)
	ZtD = matmul(Zt,D)
	delA = matmul(Zinv,ZtD)
	for i in range(len(A)):
		A[i] = A[i] + delA[i][0]

print ("")
'''for i in range(len(delA)):
	print delA[i] '''
print A[0]
print A[1]
out = []
x1 = []
y1 = []
x1.append(0.0)
z1 = 0.1
for i in range(25):
	x1.append(z1)
	z1 += 0.1
for i in range(len(x1)):
	y1.append(fn(x1[i],A[0],A[1]))
for i in range(len(x)):
	out.append(fn(x[i],A[0],A[1]))
	print(x[i],fn(x[i],A[0],A[1]))

with open('output1.txt','w') as f:
	f.writelines(map("{} {}\n".format,x,out))
	
with open('output2.txt','w') as f:
	f.writelines(map("{} {}\n".format,x1,y1))

import matplotlib.pyplot as plt
plt.plot(x1,y1)
plt.scatter(x,out)
plt.show()






	
