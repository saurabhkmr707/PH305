del_x = 0.1
T0 = 0
Tn = 10
n = int((Tn-T0)/del_x - 1) + 2

def rk4(n,del_x,z1):
	Ta = 20.
	h_ = 0.01

	x = [0.0 for i in range(n)]
	z = [0.0 for i in range(n)]
	T = [0.0 for i in range(n)]

	x[0] = 0.
	z[0] = z1
	T[0] = 40.

	for i in range(1,n):
		x[i] = x[i-1] + del_x

	for i in range(1,n):
		k1 = h_*(T[i-1] - Ta)
		k2 = -h_*Ta + h_*(T[i-1] + z[i-1]*del_x/2.)
		k3 = -h_*Ta + h_*(T[i-1] + z[i-1]*del_x/2.)
		k4 = -h_*Ta + h_*(T[i-1] + z[i-1]*del_x)
		k = (1./6.)*(k1 + 2*k2 + 2*k3 + k4)
		z[i] = z[i-1] + k*del_x
	
		k1 = z[i-1]
		k2 = z[i-1] + h_*(T[i-1]-Ta)*del_x/2.
		k3 = z[i-1] + h_*(T[i-1]-Ta)*del_x/2.
		k4 = z[i-1] + h_*(T[i-1]-Ta)*del_x
		k = (1./6.)*(k1 + 2*k2 + 2*k3 + k4)
		T[i] = T[i-1] + k*del_x	
	temp = T
	x1 = x
	return temp,x1
z1 = 10.
z2 = 20.
Ti,x = rk4(n,del_x,z1)
T1 = Ti[len(Ti)-1]

Tf,x = rk4(n,del_x,z2)
T2 = Tf[len(Tf)-1]

z = z1 + ((z2-z1)/(T2-T1))*(200. - T1)

T,x = rk4(n,del_x,z)
with open('output.txt','w') as f:
	f.writelines(map("{} {} {} {}\n".format,x,Ti,Tf,T))
import matplotlib.pyplot as plt
plt.plot(x,T)
plt.show()
print (T[len(T)-2])
