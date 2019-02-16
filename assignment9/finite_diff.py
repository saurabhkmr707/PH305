import copy
def gausjordan(a):
    I = [[1 if i == x else 0 for i in range(len(a))] for x in range(len(a))]
    n=len(a)
    for i in range(len(a)):
        
        
        for k in range(i+1,len(a)):
            c=a[k][i]/a[i][i]
            for j in range(len(a[i])):
                a[k][j]=a[k][j]-c*a[i][j]
                if j != n:
                    I[k][j]=I[k][j]-c*I[i][j]
    for i in range(len(a)-1,-1,-1):
        for k in range(i-1,-1,-1):
            lam=a[k][i]/a[i][i]
            for j in range(len(a[i])):
                a[k][j]=a[k][j]-lam*a[i][j]
                if j != n:
                    I[k][j]=I[k][j]-lam*I[i][j]

    for i in range(len(a)):
        m=a[i][i]
        for z in range(len(a)+1):
            if z != len(a):
                I[i][z]=I[i][z]/m  
                
            a[i][z] = a[i][z]/m 
                
    
   
    return (a,I)
    
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
import matplotlib.pyplot as plt
T0 = 0.
Tn = 10.
n = 10
del_x = (Tn-T0)/(n+1.)
print del_x

#n = 20
T = [[0. for i in range(n+1)] for i in range(n)]

	
h_ = 0.01
Ta = 20.

for i in range(n):
	for j in range(n):
		if (i == j):
			T[i][j] = (2. + h_*del_x**2.) 	
		elif (j == i+1):
			T[i][j] = -1.
		elif (i == j+1):
			T[i][j] = -1.
T[0][n] = 40. + Ta*h_*(del_x**2.)
T[n-1][n] = 200. + Ta*h_*(del_x**2.)

for i in range(1,n-1):
	T[i][n] = Ta*h_*(del_x**2.)

for i in range(len(T)):
	print T[i]

a1,I = gausjordan(T)
sol = []
for i in range(len(a1)):
	sol.append(a1[i][-1])
x = [0.0 for i in range(len(sol))]
x[0] = del_x
for i in range(len(x)):
	x[i] = x[i-1]+del_x
plt.plot(x,sol)
plt.show()
for i in range(len(sol)):
	print sol[i]
	print x[i]

with open('output1.txt','w') as f:
	f.writelines(map("{} {}\n".format,x,sol))
