
#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

double T(double x,double y){ return 2*x*y + 2*x - x*x - 2*y*y + 72; }

int main(){
double xl=8, yl=6;
double nx=7, ny=7;
double hx = xl/(nx-1), hy= yl/(ny-1);

double integral=0.0;
double y=0.0;
int p=1,q=1;
for(int i=0; i< ny;i=i+1,y=y+hy){
	if(i==0 or i==ny-1) p=1;
	else if(i%2) p=4;
	else p=2; 
	double x=0.0;
	for(int j=0;j< nx;j=j+1,x=x+hx){ // for x
		if(j==0 or j==nx-1) q=1;
		else if(j%2) q=4;
		else q=2; 
		integral = integral + p*q*T(x,y);
	}
}

integral = integral*hx*hy/9.0;
cout << integral;

return 0;
}

