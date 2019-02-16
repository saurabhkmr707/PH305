import numpy as np 
n = 4                                       
L = np.zeros([n,n],dtype=float)    
A = np.zeros([n,n],dtype=float)    

e = []

for line in open('val.txt'):
    e.append([float(x) for x in line.split()])     

A = np.array(e)

print("Matrix A")
print(A)
print()


for i in range(n):
    for j in range(i+1):
        if i==j:
            sum=0.0
            for k in range(j):
                sum=sum+(L[j,k]**2)
            L[j,j]=(A[j,j]-sum)**0.5
        else:
            sum=0.0
            for k in range(j):
                sum=sum+(L[j,k]*L[i,k])
            L[i,j]=(A[i,j]-sum)/L[j,j]

print("The calculated lower triangular matrix")
print(L)
print()

print("The product of L and transpose of L")
print(np.matmul(L,L.transpose()))
print()

print("So, A is equal to the product of L and transpose of L")