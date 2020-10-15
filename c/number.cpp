#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char * argv[])
{
	uint64_t a;
	cin>>a;
	uint64_t x[1024];
	for(uint64_t i=0; i<1024;i++)
		x[i]=1;
	uint64_t j = 0;
	uint64_t b = uint64_t(sqrt(a));
	for(uint64_t i=2; i<=b; i++)
	{	
		bool flag = false;
		//cout<<"i = "<<i<<" a= "<<a<<endl;
		while(a%i==0){
			cout<<"a "<<a<<" i "<<i<<endl;
			flag = true;
			a = a/i;
			x[j]=x[j]*i;
		}
		if(flag)
			j++;
	}
	if(a!=1){
		x[j]=a;
		j++;
	}
	//cout<<" j="<<j<<endl;
	for(uint64_t i=0; i<j;i++)
		cout<<x[i]<<" ";
	cout<<endl;
}
