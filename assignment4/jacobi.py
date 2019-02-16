import copy
a = []
with open('input.txt','r') as f:
	for line in f:
		inner_list = [elt.strip() for elt in line.split( )]
		inner_list = map(float,inner_list)
		a.append(inner_list)
		
def row_swap(matrix,a,b):
	temp = matrix
	temp[a] = matrix[b]
	temp[b] = matrix[a]
	return temp
#print (a)
#changing a to diagonally dominant matrix
atemp = []
for i in range(len(a)):
	maxx = 0
	for j in range(len(a)):
		if (abs(a[i][j])>maxx):
			maxx = a[i][j]
			temp = j
	atemp.append(a[temp])
a = list(atemp)
print a
	
b = []
a1 = []
for i in range(len(a)):
	b.append(a[i][-1])
for i in range(len(a)):
	a1.append(a[i][:-1])
#print a1
#print (b)
def jacobi(a,b):
	X = [0.0 for x in range(len(a))]
	Xprev = [0.0 for x in range(len(a))]
	flag = 0
	count = 1
	open('output_jacobi.txt','w').close()
	while(True):
		for i in range(len(a)):
			summ = 0.0
			for j in range(len(a)):
				if ( i != j):
					summ += a[i][j]*Xprev[j]
			X[i] = (b[i]-summ)/a[i][i]
			with open('output_jacobi.txt','a') as f:
				f.write(str(count)+ ' ')
				f.writelines([str(x)+' ' for x in X])
				f.write('\n')
			count += 1
		for i in range(len(a)):
			if (abs(X[i]-Xprev[i]) <= 0.0000000001):
				flag = 1
		if (flag == 1):
			break
		Xprev = list(X)
		#print X
	return X
output = jacobi(a1,b)
print (output)
