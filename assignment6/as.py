# Lab No: 5
# Title : jacobi
# Date: 29/08/2017
# Name : Anurag Sonthalia
# Roll No: 150122004
# Email : anurag.sonthalia@iitg.ernet.in


# Importing the necessary packages
import numpy as np
import copy
import sys


# Finding the max off diagonal element in A(H)
def maxa(A):
	n=len(A)
	m=0;p=-1;q=-1
	for i in range(n):
		for j in range(i+1,n):
			if abs(A[i][j])>m:
				m=abs(A[i][j])
				p=i
				q=j
	return m,p,q

# Rotating the H matrix to obtain the eigenvalues
def rotate(A,p,q,V):
	d=copy.deepcopy(A)
	n=len(A)
	Xp=[0.0]*n;Xq=[0.0]*n

	Theta=(A[q][q]-A[p][p])/(2*A[p][q])                              # Finding the theta
	t=1.0/(abs(Theta)+np.sqrt(Theta**2+1))                           # Finding the t
	if Theta<0:
		t=-t
	c=1.0/np.sqrt(t**2+1.0)                                          # Finding the c                                               
	s=c*t                                                            # Finding the s

	d[p][q]=0.0;d[q][p]=0.0                                          # Applying
	
	d[p][p]=((c**2)*A[p][p])+((s**2)*A[q][q])-(2*s*c*A[p][q])        # the
	d[q][q]=((s**2)*A[p][p])+((c**2)*A[q][q])+(2*s*c*A[p][q])        # formula
	
	for i in range(n):
		if (i!=p) and (i!=q):
			d[i][p]=c*A[i][p]-s*A[i][q]
			d[p][i]=d[i][p]
			d[i][q]=c*A[i][q]+s*A[i][p]
			d[q][i]=d[i][q]

	for i in range(n):
		Xp[i]=V[i][p]
		Xq[i]=V[i][q]

	for i in range(n):
		V[i][p]=c*Xp[i]-s*Xq[i]
		V[i][q]=s*Xp[i]+c*Xq[i]

	return d,V



# Main Function
if __name__ == '__main__':

# Making the H0 matrix
	n=5
	H0=[[0.0 for i in range(n)] for j in range(n)]
	for i in range(n):
		for j in range(n):
			if i==j:
				H0[i][j]=(i+1/2)
	H0=np.array(H0)
	print("H0 Matrix:")
	print(H0)


# Creating the X matrix
	X=[[0.0 for i in range(n)] for j in range(n)]
	for i in range(n):
		for j in range(n):
			l=0.0
			r=0.0
			if i==(j+1):
				l=np.sqrt(j+1)/np.sqrt(2)
			if i==(j-1):
				r=np.sqrt(j)/np.sqrt(2)
			X[i][j]=l+r
	X=np.array(X)

	print("X matrix:")
	print(X)

# Creating X^4 matrix
	x4=np.identity(5)
	for i in range(4):
		x4=np.dot(x4,X)

	x4=np.array(x4)

	lamb=0.0
	out=[]
	while(lamb<=1):
		H=H0+lamb*x4
		H=np.array(H)
		
		print("\nFor lambda = %f:"%lamb)
		print("\nH matrix:")
		print(H)
		V=np.identity(len(H))
		
# Jacobis Iteration method 
		H = np.array([[8, -1, 3, -1],
		[-1, 6, 2, 0],
		[3, 2, 9, 1],
		[-1, 0, 1, 7]
		])
		for i in range(1000):
			m,p,q=maxa(H)
			if m<10**-20:
				break
			#print("Step %d :"%(i+1))
			H,V=rotate(H,p,q,V)
		
		print("\nConverged H matrix:")
		print(np.around(H,decimals=5))
		print("\nEigen Values:")
		print(np.diagonal(H))
		#print("\nEigen Vectors:")
		#print(V)
		s=[i for i in np.diagonal(H)]
		out+=[[lamb]+sorted(s)]
		lamb+=0.1

	# Saving the output in a file fort.10
	f=open("fort.10",'w')
	sys.stdout=f
	for i in out:
		for j in i:
			print("%.5f"%j,end='   ')
		print(" ")	
	f.close()

